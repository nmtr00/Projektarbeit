# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by caber on Sun May 12 23:08:30 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=196.823425292969, 
    height=222.366668701172)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('SImu1.cae')
#: The model database "F:\Projektarbeit\abaqus file\SImu1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='contact')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o1 = session.openOdb(
    name='E:/SIMULIA/simulation_parametric/press1_variation_c1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: E:/SIMULIA/simulation_parametric/press1_variation_c1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          10
#: Number of Steps:              2
odb = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c1.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial displacement: U2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy2 = combine(xy0, xy1, )
xy_result = session.XYData(name='XYData-1', objectToCopy=xy2, 
    sourceDescription='combine(XYData-1, XYData-1, )')
del session.xyDataObjects[xy0.name]
del session.xyDataObjects[xy1.name]
del session.xyDataObjects[xy2.name]
c1 = session.Curve(xyData=xy_result)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.889997, 0, 0, -0.0134824, 0, 0.889997, 0, -0.0181393, 0, 0, 
    0.889997, 0, 0, 0, 0, 1))
session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c1.odb'].close(
    )
o1 = session.openOdb(
    name='E:/SIMULIA/simulation_parametric/press1_variation_c113.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: E:/SIMULIA/simulation_parametric/press1_variation_c113.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          10
#: Number of Steps:              2
odb = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c113.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial displacement: U2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy2 = combine(xy0, xy1, )
xy_result = session.XYData(name='XYData-2', objectToCopy=xy2, 
    sourceDescription='combine(XYData-2, XYData-2, )')
del session.xyDataObjects[xy0.name]
del session.xyDataObjects[xy1.name]
del session.xyDataObjects[xy2.name]
c1 = session.Curve(xyData=xy_result)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
o1 = session.openOdb(
    name='E:/SIMULIA/simulation_parametric/press1_variation_c13.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: E:/SIMULIA/simulation_parametric/press1_variation_c13.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          10
#: Number of Steps:              2
odb = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c13.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial displacement: U2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
xy2 = combine(xy0, xy1, )
xy_result = session.XYData(name='XYData-3', objectToCopy=xy2, 
    sourceDescription='combine(XYData-3, XYData-3, )')
del session.xyDataObjects[xy0.name]
del session.xyDataObjects[xy1.name]
del session.xyDataObjects[xy2.name]
c1 = session.Curve(xyData=xy_result)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c113.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c13.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* VisError: The output database 
#* E:/SIMULIA/simulation_parametric/press1_variation_c13.odb disk file has 
#* changed.
#* 
#* The current plot operation has been canceled, re-open the file to view the 
#* results
o7 = session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c113.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.27647, 
    farPlane=0.412399, width=0.0963123, height=0.0435232, 
    viewOffsetX=-0.00191586, viewOffsetY=0.000910399)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['layer']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['plate']
p.deleteMesh()
p = mdb.models['Model-1'].parts['plate']
p.seedPart(size=0.0001, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['plate']
p.seedPart(size=0.001, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['plate']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    nodeLabels=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.15676, 
    farPlane=0.16573, width=0.0601783, height=0.0272471, 
    viewOffsetX=0.000347702, viewOffsetY=0.00170766)
mdb.save()
#: The model database has been saved to "F:\Projektarbeit\abaqus file\SImu1.cae".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.150296, 
    farPlane=0.172195, width=0.146841, height=0.0663569, viewOffsetX=0.0305845, 
    viewOffsetY=0.0181899)
p = mdb.models['Model-1'].parts['plate']
n = p.nodes
nodes = n.getSequenceFromMask(mask=('[#ffffffff:27 #7ffffff ]', ), )
p.Set(nodes=nodes, name='all_nodes')
#: The set 'all_nodes' has been edited (891 nodes).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.156757, 
    farPlane=0.165733, width=0.0534936, height=0.0241736, viewOffsetX=0.011706, 
    viewOffsetY=0.0095603)
p = mdb.models['Model-1'].parts['plate']
n = p.nodes
nodes = n.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(nodes=nodes, name='one_node')
#: The set 'one_node' has been edited (1 node).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.152574, 
    farPlane=0.169916, width=0.116384, height=0.0525935, viewOffsetX=0.0192281, 
    viewOffsetY=0.0143103)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['press1'].submit(consistencyChecking=OFF)
#: The job input file "press1.inp" has been submitted for analysis.
#: Job press1: Analysis Input File Processor completed successfully.
#: Job press1: Abaqus/Standard completed successfully.
#: Job press1 completed successfully. 
mdb.Job(name='press2', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=6, numDomains=6, numGPUs=0)
mdb.jobs['press2'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "press2.inp".
mdb.jobs['press2'].submit(consistencyChecking=OFF)
#: The job input file "press2.inp" has been submitted for analysis.
#: Job press2: Analysis Input File Processor completed successfully.
#: Job press2: Abaqus/Standard completed successfully.
#: Job press2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/SIMULIA/simulation_parametric/press1_variation_c113.odb'])
o3 = session.openOdb(name='F:/Projektarbeit/abaqus file/press2.odb')
#: Model: F:/Projektarbeit/abaqus file/press2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          10
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['F:/Projektarbeit/abaqus file/press2.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF2 PI: PLATE-1 Node 2 in NSET ONE_NODE', 
    suppressQuery=True, __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['F:/Projektarbeit/abaqus file/press2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.282242, 
    farPlane=0.406627, width=0.0191225, height=0.00864137, 
    viewOffsetX=-0.0109101, viewOffsetY=-0.0079179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.282149, 
    farPlane=0.40672, width=0.0191625, height=0.00865945, 
    viewOffsetX=-0.0109065, viewOffsetY=-0.00791528)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-0.00345648, 
    viewOffsetY=-0.00804508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.278045, 
    farPlane=0.410824, width=0.0834109, height=0.0376931, 
    viewOffsetX=0.00364413, viewOffsetY=-0.000276125)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=100 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.278799, 
    farPlane=0.41007, width=0.0579348, height=0.0261805, 
    viewOffsetX=0.00712535, viewOffsetY=-0.00549507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268151, 
    farPlane=0.416847, width=0.0557221, height=0.0251806, cameraPosition=(
    -0.0059863, 0.065126, 0.337464), cameraUpVector=(-0.0638804, 0.991027, 
    -0.117408), cameraTarget=(0.0396621, 0.0278645, -0.0018924), 
    viewOffsetX=0.00685321, viewOffsetY=-0.0052852)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268327, 
    farPlane=0.41667, width=0.0557587, height=0.0251972, cameraPosition=(
    -0.00557698, 0.0657016, 0.337456), cameraUpVector=(-0.00057524, 0.994017, 
    -0.109221), cameraTarget=(0.0400714, 0.0284401, -0.00190055), 
    viewOffsetX=0.00685772, viewOffsetY=-0.00528868)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.265744, 
    farPlane=0.428931, width=0.055222, height=0.0249546, cameraPosition=(
    0.164105, 0.0286797, 0.324415), cameraUpVector=(-0.0548159, 0.998294, 
    0.020124), cameraTarget=(0.0392792, 0.0282968, 0.00339568), 
    viewOffsetX=0.0067917, viewOffsetY=-0.00523777)
