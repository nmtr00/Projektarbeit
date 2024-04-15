import pandas as pd
import os
import matplotlib.pyplot as plt

log_file_path = ".\Druckversuch_data\Test.txt"
with open(log_file_path, 'r') as file:
    log_data = file.read()
    
# Filter out lines with unwanted values
filtered_lines = [line for line in log_data.split('\n') if not any(x in line for x in ['-1|-1|-1','-2|-2|-2', '-3|-3|-3'])]

#create a list to store datarows
rows =[line.split('|') for line in filtered_lines[1:]]
column_names = ['Zeit', 'Kraft', 'Abstand']

df = pd.DataFrame(rows, columns= column_names)

file_name = os.path.splitext(os.path.basename(log_file_path))[0]

csv_file_path = f'.\Druckversuch_data\{file_name}.csv'
df.to_csv(csv_file_path, index=False)

df['Kraft'] = pd.to_numeric(df['Kraft'])
df['Abstand'] = pd.to_numeric(df['Abstand'])
df['Zeit'] = pd.to_numeric(df['Zeit'])
plt.plot(df['Abstand'], df['Kraft'], linestyle = '-')
plt.xlabel('Abstand')
plt.ylabel('Kraft')

# Set x-axis and y-axis grid resolution
plt.xticks(range(int(min(df['Abstand'])), int(max(df['Abstand'])) + 1, 5))
plt.yticks(range(int(min(df['Kraft'])), int(max(df['Kraft'])) + 1, 200))


plt.grid(True)

plt.show()
