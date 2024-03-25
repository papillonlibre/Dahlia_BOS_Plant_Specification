import os
import pandas as pd

def combine_csv_files(folder_path, output_file):
    # Get a list of all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Iterate through each CSV file
    for file in csv_files:
        # Read the CSV file into a DataFrame
        file_path = os.path.join(folder_path, file)
        data = pd.read_csv(file_path)
        dataframes.append(data)

    # Concatenate all DataFrames into a single DataFrame
    combined_data = pd.concat(dataframes, ignore_index=True)

    # Write the combined DataFrame to a new CSV file
    combined_data.to_csv(output_file, index=False)
    print(f"Combined data written to '{output_file}'")

# Example usage:
folder_path = 'D:\Dahlia_BOS_Plant_Specification\model_inference_2'
output_file = 'combined_data.csv'
combine_csv_files(folder_path, output_file)
