# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import glob
import os


#%% To do that accross all the participants


def extract_desired_portion(filename):
    # Split the filename using the backslash as the separator
    split_filename = filename.split('\\')

    # Get the last element from the split_filename list, which contains the desired portion
    desired_portion = split_filename[-1]

    # Remove the file extension from the desired portion
    desired_portion = desired_portion.replace('.wav', '')

    return desired_portion







#%% SCRIPT

# Create an empty DataFrame to store the results
result_df = pd.DataFrame(columns=['Filename', 'Mean', 'Std', 'Min', 'Max','mean_10Hz','mean_20Hz','mean_30Hz','mean_40Hz','mean_60Hz','mean_80Hz','mean_90Hz'])

# Define the path to the directory containing the CSV files
csv_directory = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_questionnaires/'

# Define the file pattern for CSV files
csv_pattern = '*.csv'

# Get a list of all CSV files in the directory
csv_files = glob.glob(csv_directory + csv_pattern)

# Iterate over each CSV file
for file in csv_files:
    # Read the DataFrame from the CSV file
    df = pd.read_csv(file)
    
    # Assuming you have a column named 'column_name'
    # Replace 'column_name' with the actual name of your column

    # Apply the filename transformation to the 'Filename' column using apply() and a lambda function
    df['New Trial'] = df['New Trial'].apply(lambda x: extract_desired_portion(x))

    # Print the updated DataFrame

    
    # Calculate the mean, standard deviation, minimum, and maximum of the column
    column_mean = df['Slider MarkerPos'].mean()
    column_std = df['Slider MarkerPos'].std()
    column_min = df['Slider MarkerPos'].min()
    column_max = df['Slider MarkerPos'].max()

    condition1 = df['New Trial'] == '10Hz'
    condition2 = df['New Trial'] == '20Hz'
    condition3 = df['New Trial'] == '30Hz'
    condition4 = df['New Trial'] == '40Hz'
    condition5 = df['New Trial'] == '60Hz'
    condition6 = df['New Trial'] == '80Hz'
    condition7 = df['New Trial'] == '90Hz'

    mean_10Hz = df[condition1]['Slider MarkerPos'].mean()
    mean_20Hz = df[condition2]['Slider MarkerPos'].mean()
    mean_30Hz = df[condition3]['Slider MarkerPos'].mean()
    mean_40Hz = df[condition4]['Slider MarkerPos'].mean()
    mean_60Hz = df[condition5]['Slider MarkerPos'].mean()
    mean_80Hz = df[condition6]['Slider MarkerPos'].mean()
    mean_90Hz = df[condition7]['Slider MarkerPos'].mean()


    # Extract the filename without the extension
    filename = os.path.splitext(os.path.basename(file))[0]
    
    # Create a temporary DataFrame with the filename and statistics
    temp_df = pd.DataFrame({
        'Filename': [filename],
        'Mean': [column_mean],
        'Std': [column_std],
        'Min': [column_min],
        'Max': [column_max],
        'mean_10Hz': [mean_10Hz],
        'mean_20Hz': [mean_20Hz],
        'mean_30Hz': [mean_30Hz],
        'mean_40Hz': [mean_40Hz],
        'mean_60Hz': [mean_60Hz],
        'mean_80Hz': [mean_80Hz],
        'mean_90Hz': [mean_90Hz],
    })
    
    # Concatenate the temporary DataFrame with the result DataFrame
    result_df = pd.concat([result_df, temp_df], ignore_index=True)

# Print the result DataFrame
print(result_df)

len(result_df)
#%%

# Assuming your DataFrame is named 'df'
result_df = result_df.set_index(result_df.index + 1)

print(result_df)
#%%

# Read the second CSV file
df2 = pd.read_csv('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/STAT_IDA.csv')


result_df = result_df.rename(columns={'Filename': 'Code'})

# Specify the column names to match
column_names = ['Code']  # Replace with the actual column names

# Merge the two DataFrames based on the matching columns
merged_df = pd.merge(result_df, df2, on=column_names, how='outer', indicator=False)

# Print the merged DataFrame
print(merged_df)

len(merged_df)
#%%

output_file_name = 'TOTAL'

#%%
# Save the subset DataFrame to a new CSV file with the provided name
csv_file_path = f"C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/{output_file_name}.csv"
merged_df.to_csv(csv_file_path, index=False)
# %%
