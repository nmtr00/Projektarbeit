import os
import glob
import subprocess
from datetime import datetime
import time
import platform

# Base folder path
folder_path = './'

# Directory to store generated scripts
script_dir = os.path.join(folder_path, 'abaqus_scripts')
if not os.path.exists(script_dir):
    os.makedirs(script_dir)

# Directory to store generated report files
report_dir = os.path.join(folder_path, 'abaqus_reports')
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

# Date for the script header
date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Find all .odb files in the folder
odb_files = glob.glob(os.path.join(folder_path, '*.odb'))

# Script template
script_template = """

from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup

executeOnCaeStartup()

# Open the ODB file
odb_path = '{odb_path}'

o2 = session.openOdb(name=odb_path)
# Extract XY data from the history output
xy_displacement = xyPlot.XYDataFromHistory(
    odb=o2, 
    outputVariableName='Spatial displacement: U2 PI: PLATE-1 Node 1 in NSET UNDER_NODE', 
    steps=('press', ), 
    suppressQuery=True, 
    __linkedVpName__='Viewport: 1'
)

xy_contact_force = xyPlot.XYDataFromHistory(
    odb=o2, 
    outputVariableName='CFT2: CFT2     General_Contact_Faces/General_Contact_Faces', 
    steps=('press', ), 
    suppressQuery=True, 
    __linkedVpName__='Viewport: 1'
)
xy_area = xyPlot.XYDataFromHistory(
    odb=o2, 
    outputVariableName='Total area in contact: CAREA    General_Contact_Faces/General_Contact_Faces', 
    steps=('press', ), 
    suppressQuery=True, 
    __linkedVpName__='Viewport: 1'
)

# Create curves for each dataset
curve_displacement = session.Curve(xyData=xy_displacement)
curve_contact_force = session.Curve(xyData=xy_contact_force)
curve_area = session.Curve(xyData=xy_area)

# Combine the XY data
combined_xy_data_force = combine(xy_displacement, xy_contact_force)
xy_result_force = session.XYData(
    name='CombinedXYData_force', 
    objectToCopy=combined_xy_data_force, 
    sourceDescription='combine(xy_displacement, xy_contact_force)'
)
combined_xy_data_area = combine(xy_displacement, xy_area)
xy_result_area = session.XYData(
    name='CombinedXYData-area', 
    objectToCopy=combined_xy_data_area, 
    sourceDescription='combine(xy_displacement, xy_area)'
)

# Clean up temporary XY data objects
del session.xyDataObjects[xy_displacement.name]
del session.xyDataObjects[xy_contact_force.name]
del session.xyDataObjects[xy_area.name]
del session.xyDataObjects[combined_xy_data_force.name]
del session.xyDataObjects[combined_xy_data_area.name]



# Write the XY data to report files
report_force = '{report_force}'
session.xyReportOptions.setValues(layout=SINGLE_TABLE)
session.writeXYReport(fileName=report_force, xyData=(xy_result_force, ))
report_area = '{report_area}'
session.xyReportOptions.setValues(layout=SINGLE_TABLE)
session.writeXYReport(fileName=report_area, xyData=(xy_result_area, ))

o2.close()
"""

# Loop through each .odb file
for odb_path in odb_files:
    # Get the base name of the .odb file (e.g., 'curve_test_variation_c1')
    base_name = os.path.splitext(os.path.basename(odb_path))[0]
    script_file = os.path.join(script_dir, f'script_{base_name}.py')
    report_force = os.path.join(report_dir, f'{base_name}_force.csv')
    report_area = os.path.join(report_dir, f'{base_name}_area.csv')
    
    # Generate script content
    script_content = script_template.format(
        date=date_str,
        odb_path=odb_path,
        report_force=report_force,
        report_area=report_area
    )
    
    # Write script to file
    with open(script_file, 'w') as f:
        f.write(script_content)
    
    # Run the generated script with Abaqus CAE
    command = f'abaqus viewer noGUI={script_file}'
    
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script for {base_name}: {e}")


# Clean up Abaqus replay files
if platform.system() == 'Windows':
    cleanup_command = 'del abaqus.rpy.*'
else:
    cleanup_command = 'rm abaqus.rpy.*'
try:
    subprocess.run(cleanup_command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error cleaning up Abaqus replay files: {e}")

