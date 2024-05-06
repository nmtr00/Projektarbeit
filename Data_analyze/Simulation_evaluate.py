import pandas as pd

# Define a function to convert scientific notation to decimal
def sci_to_dec(value):
    try:
        # Attempt to convert the value from scientific notation
        mantissa, exponent = value.split('E')
        mantissa = float(mantissa)
        exponent = int(exponent)
        return round(mantissa * (10 ** (exponent + 3)),10)
    except ValueError:
        # If conversion fails, return the original value as a float
        return float(value)
def sci_to_dec1(value):
    try:
        # Attempt to convert the value from scientific notation
        mantissa, exponent = value.split('E')
        mantissa = float(mantissa)
        exponent = int(exponent)
        return round(mantissa * (10 ** (exponent)),10)
    except ValueError:
        # If conversion fails, return the original value as a float
        return float(value)

def main():



# Open the report file
with open(r"C:\Abaqus\press\Neo_1700000_6,5E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df = pd.DataFrame(rows, columns=['weg', 'kraft'])

# Convert the column to a Series
#column_series = df['weg']

# Display the column without row numbering
#print(column_series.head(101).to_string(index=False))
with open(r"C:\Abaqus\press\Neo_1800000_6,5E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df2 = pd.DataFrame(rows, columns=['weg', 'kraft'])
df2
with open(r"C:\Abaqus\press\Neo_1600000_6,5E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df3 = pd.DataFrame(rows, columns=['weg', 'kraft'])
df3
with open("C:\Abaqus\press\data_versuch.csv") as file1:
    # Read each line of the report
    rows1 = []
    for line in file1:
        # Split the line into two values
        value3, value4 = line.split(";")
        value4 = value4.rstrip('\n')
        value3 = float(value3)
        value4 = float(value4)
        rows1.append([value3, value4])
        
# Create a pandas DataFrame from the data
df1 = pd.DataFrame(rows1, columns=['weg', 'kraft'])
df1

import matplotlib.pyplot as plt

plt.plot(df3['weg'], df3['kraft'], color='blue', label='Line 16 Plot')
plt.plot(df['weg'], df['kraft'], color='red', label='Line 17 Plot')
plt.plot(df2['weg'], df2['kraft'], color='green', label='Line 18 Plot')
plt.scatter(df1['weg'], df1['kraft'], label='Scatter Plot')

# Add labels and title
plt.xlabel('weg')
plt.ylabel('kraft')
plt.title('Line Plot of weg vs kraft')


# Show the plot
plt.legend()
plt.show()
with open(r"C:\Abaqus\press\Neo_1600000_5,5E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df4 = pd.DataFrame(rows, columns=['weg', 'kraft'])

with open(r"C:\Abaqus\press\Neo_1600000_6E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df5 = pd.DataFrame(rows, columns=['weg', 'kraft'])

with open(r"C:\Abaqus\press\Neo_1600000_7E-7.csv") as file:
    # Read each line of the report
    rows = []
    for line in file:
        # Split the line into two values
        value1, value2 = line.strip().split()
        # Convert the scientific notation to decimal for value1
        value1_decimal = sci_to_dec(value1)
        value2_full = sci_to_dec1(value2)
        rows.append([value1_decimal, value2_full])
        
# Create a pandas DataFrame from the data
df6 = pd.DataFrame(rows, columns=['weg', 'kraft'])

import matplotlib.pyplot as plt

plt.plot(df3['weg'], df3['kraft'], color='blue', label='Line 6,5 Plot')
plt.plot(df4['weg'], df4['kraft'], color='red', label='Line 5,5 Plot')
plt.plot(df5['weg'], df5['kraft'], color='green', label='Line 6 Plot')
plt.plot(df6['weg'], df6['kraft'], color='black', label='Line 7 Plot')
plt.scatter(df1['weg'], df1['kraft'], label='Scatter Plot')

# Add labels and title
plt.xlabel('weg')
plt.ylabel('kraft')
plt.title('Line Plot of weg vs kraft')


# Show the plot
plt.legend()
plt.show()