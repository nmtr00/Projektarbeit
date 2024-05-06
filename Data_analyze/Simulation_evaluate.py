import pandas as pd
import os
import matplotlib.pyplot as plt



input_folder = "."
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
    all_data = []

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            filename_without_extension = os.path.splitext(filename)[0]
            print("Processing video:", filename)
           
            rows = []
            # No need to close loading_bar here, it's automatically closed when exiting the "with" block
            with open(file_path) as file:
            # Read each line of the report
                
                for line in file:
                    # Split the line into two values
                    value1, value2 = line.strip().split()
                    # Convert the scientific notation to decimal for value1
                    value1_decimal = sci_to_dec(value1)
                    value2_full = sci_to_dec1(value2)
                    rows.append([value1_decimal, value2_full])
                
                    # Create a pandas DataFrame from the data
                    df = pd.DataFrame(rows, columns=['weg', 'kraft'])
                    all_data.append((filename_without_extension, df))
            
            
            with open(f"{input_folder}\data_versuch.csv") as file1:
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
                df_measured = pd.DataFrame(rows1, columns=['weg', 'kraft'])
            
# Plot all the data
    for filename_without_extension, df in all_data:
        plt.plot(df['Weg'], df['Kraft'], label=filename_without_extension)

    plt.scatter(df_measured['Weg'], df_measured['Kraft'], color='black', label='Measured Data')

    # Add labels and title
    plt.xlabel('Weg')
    plt.ylabel('Kraft')
    plt.title('Graph of Weg vs Kraft')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()

main()


