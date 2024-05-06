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
        return round(mantissa * (10 ** (exponent + 3)), 10)
    except ValueError:
        # If conversion fails, return the original value as a float
        return float(value)

def sci_to_dec1(value):
    try:
        # Attempt to convert the value from scientific notation
        mantissa, exponent = value.split('E')
        mantissa = float(mantissa)
        exponent = int(exponent)
        return round(mantissa * (10 ** exponent), 10)
    except ValueError:
        # If conversion fails, return the original value as a float
        return float(value)

def main():
    all_data = []  # List to store all dataframes

    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            filename_without_extension = os.path.splitext(filename)[0]
            print("Processing file:", filename)

            # Read data from the CSV file
            rows = []
            with open(file_path) as file:
                for line in file:
                    value1, value2 = line.strip().split()
                    value1_decimal = sci_to_dec(value1)
                    value2_full = sci_to_dec1(value2)
                    rows.append([value1_decimal, value2_full])

            # Create a pandas DataFrame from the data
            df = pd.DataFrame(rows, columns=['Weg', 'Kraft'])
            all_data.append((filename_without_extension, df))

    # Read and plot measured data
    rows_measured = []
    with open(os.path.join(input_folder, "data_versuch.csv")) as file1:
        for line in file1:
            value3, value4 = line.split(";")
            value4 = value4.rstrip('\n')
            value3 = float(value3)
            value4 = float(value4)
            rows_measured.append([value3, value4])

    df_measured = pd.DataFrame(rows_measured, columns=['Weg', 'Kraft'])

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
