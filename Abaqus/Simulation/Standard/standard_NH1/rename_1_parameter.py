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
        value1 = match.group(2)  # Parameter value (e.g., 100000.0, 150000.0, ...)
        #value2 = match.group(3)

        parameter_values[param] = (value1)
count1 = 0 
count2 = 0
for param, (value1) in parameter_values.items():

    pattern1 = os.path.join(files_directory, f'*c{param}_force.csv')
    files1 = glob.glob(pattern1)
    

    if not files1:
        print(f'No force data found for parameter: c{param}')
        continue

    
    for old_file_path_1 in files1:
        count1 += 1
        old_file_name_1 = os.path.basename(old_file_path_1)
        new_file_name_1 = old_file_name_1.replace(f'c{param}_force.csv', f'[{value1}]_force.csv')

        new_file_path = os.path.join(files_directory, new_file_name_1)

        # Rename the file
     
        os.rename(old_file_path_1, new_file_path)
        print(f'Renamed: {old_file_name_1} -> {new_file_name_1}')

for param, (value1) in parameter_values.items():

    pattern2 = os.path.join(files_directory, f'*c{param}_area.csv')
    files2 = glob.glob(pattern2)

    if not files2:
        print(f'No area data found for parameter: c{param}')
        continue

    
    for old_file_path_2 in files2:
        count2 += 1
        old_file_name_2 = os.path.basename(old_file_path_2)
        new_file_name_2 = old_file_name_2.replace(f'c{param}_area.csv', f'[{value1}]_area.csv')

        new_file_path = os.path.join(files_directory, new_file_name_2)

        # Rename the file
     
        os.rename(old_file_path_2, new_file_path)
        print(f'Renamed: {old_file_name_2} -> {new_file_name_2}')

print(f'{count1} force data files are renamed')
print(f'{count2} area data files are renamed')
   

   



# # Rename the .csv files based on the extracted parameters
# for param, value in parameter_values.items():
#     old_file_name = f'R0069804_NH1_variation_c{param}.csv'
#     new_file_name = f'R0069804_NH1_variation_[{value}].csv'
    
#     old_file_path = os.path.join(files_directory, old_file_name)
#     new_file_path = os.path.join(files_directory, new_file_name)
    
#     if os.path.exists(old_file_path):
#         os.rename(old_file_path, new_file_path)
#         print(f'Renamed: {old_file_name} -> {new_file_name}')
#     else:
#         print(f'File not found: {old_file_name}')