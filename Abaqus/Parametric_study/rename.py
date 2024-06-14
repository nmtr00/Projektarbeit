import os
import re
import glob

# Path to your working directory
files_directory = '.'

#Find the log file in the working directory
log_file_path = None
for file_name in os.listdir(files_directory):
    if file_name.endswith('.log'):
        log_file_path = os.path.join(files_directory, file_name)
        break

if log_file_path is None:
    print("No log file in the directory!")
    exit(1)

# Read the log file
with open(log_file_path, 'r') as file:
    log_content = file.readlines()

# Define a dictionary to store parameter values
parameter_values = {}

# Define a regex pattern to match parameter lines
parameter_pattern = re.compile(r'\s*c(\d+)\s*=\s*\[(\d+\.\d+)\]')

# Process the log file to extract parameter values
for line in log_content:
    match = parameter_pattern.search(line)
    if match:
        param = match.group(1)  # Parameter index (e.g., 1, 2, 3, ...)
        value = match.group(2)  # Parameter value (e.g., 100000.0, 150000.0, ...)
        parameter_values[param] = value
count =0 
for param, value in parameter_values.items():

    pattern = os.path.join(files_directory, f'*c{param}.odb')
    files = glob.glob(pattern)

    if not files:
        print(f'No files found for parameter: c{param}')
        continue

    
    for old_file_path in files:
        count += 1
        old_file_name = os.path.basename(old_file_path)
        new_file_name = old_file_name.replace(f'c{param}.odb', f'[{value}].odb')

        new_file_path = os.path.join(files_directory, new_file_name)

        # Rename the file
     
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_file_name} -> {new_file_name}')

print(f'{count} simulations are renamed')
   

   



# # Rename the .odb files based on the extracted parameters
# for param, value in parameter_values.items():
#     old_file_name = f'R0069804_NH1_variation_c{param}.odb'
#     new_file_name = f'R0069804_NH1_variation_[{value}].odb'
    
#     old_file_path = os.path.join(files_directory, old_file_name)
#     new_file_path = os.path.join(files_directory, new_file_name)
    
#     if os.path.exists(old_file_path):
#         os.rename(old_file_path, new_file_path)
#         print(f'Renamed: {old_file_name} -> {new_file_name}')
#     else:
#         print(f'File not found: {old_file_name}')