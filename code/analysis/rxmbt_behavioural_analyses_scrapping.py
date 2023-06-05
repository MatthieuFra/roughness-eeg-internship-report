# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


# Specify the path to the log file
log_file_path = "C:/Users/mfratice/Documents/DATA/PSYCHOPY/roughxpmbt_2023-05-09_10h46.44.424_DP_202305098_run2/roughxpmbt_2023-05-09_10h46.44.424_DP_202305098_run2.log"
output_file_name = "GCYIJW"


# TO SCRAP THE DATAS


# Read the log file
with open(log_file_path, 'r') as file:
    log_data = file.read()

# Extract all occurrences of the patterns using regular expressions
new_trial_pattern = r"New trial \(rep=\d+, index=\d+\): {'sound_file': '([^']+)'}"
slider_pattern = r"slider: markerPos = (\d+\.\d+)"
new_trial_matches = re.findall(new_trial_pattern, log_data)
slider_matches = re.findall(slider_pattern, log_data)

# Create a dictionary to store the matches with their indices
new_trial_dict = {}
slider_dict = {}

# Iterate over the matches and store them in the dictionaries
for match in re.finditer(new_trial_pattern, log_data):
    new_trial_dict[match.start()] = match.group(1)

for match in re.finditer(slider_pattern, log_data):
    slider_dict[match.start()] = match.group(1)

# Create lists to store the final matches
new_trial_final = []
slider_final = []

# Iterate over the indices in ascending order
for idx in sorted(set(new_trial_dict.keys()) | set(slider_dict.keys())):
    new_trial_final.append(new_trial_dict.get(idx))
    slider_final.append(slider_dict.get(idx))

# Create a DataFrame with the extracted data
data = {'New Trial': new_trial_final, 'Slider MarkerPos': slider_final}
df = pd.DataFrame(data)

# Display the resulting DataFrame
print(df)




# THEN TO ALIGN DATA


# Assuming you have already created the DataFrame df

# Initialize a variable to store the aligned data
aligned_data = []

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    if row['New Trial'] is not None:
        # Find the index of the first non-null value of 'Slider MarkerPos' after the current row
        markerpos_index = df['Slider MarkerPos'].loc[index+1:].first_valid_index()
        if markerpos_index is not None:
            # Get the corresponding 'Slider MarkerPos' value
            markerpos_value = df.loc[markerpos_index, 'Slider MarkerPos']
            aligned_data.append([row['New Trial'], markerpos_value])

# Create a new DataFrame with the aligned data
aligned_df = pd.DataFrame(aligned_data, columns=['New Trial', 'Slider MarkerPos'])

# Display the aligned DataFrame
print(aligned_df)


# Save the subset DataFrame to a new CSV file with the provided name
csv_file_path = f"C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_questionnaires/{output_file_name}.csv"
aligned_df.to_csv(csv_file_path, index=False)
# %%
