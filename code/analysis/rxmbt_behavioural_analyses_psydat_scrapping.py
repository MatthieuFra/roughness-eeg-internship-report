# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import pandas as pd

from psychopy.misc import fromFile

#%%

# Specify the path to the log file
fpath = "C:/Users/mfratice/OneDrive - Institut Pasteur Paris/roughxpmbt/01_roughxpmbt_data/00_roughxpmbt_psychopy/roughxpmbt_2023-05-09_14h31.26.147_CJ20230509_run2/roughxpmbt_2023-05-09_14h31.26.147_CJ20230509_run2.psydat"
output_file_name = "TEST scrap2"


# TO SCRAP THE DATAS

# (replace with the file path to your .psydat file)
list = []
psydata = fromFile(fpath)
for entry in psydata.entries:
    list.append(entry)



def list_of_dicts_to_dataframe(data):
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Iterate over each dictionary in the list
    for d in data:
        # Append the dictionary as a new row to the DataFrame
        df = df.append(d, ignore_index=True)

    return df


df = list_of_dicts_to_dataframe(list)


df = df[['sound1','sound2', 'is_oddball', 'slider.response']]
df = df.drop([0, 1]).reset_index(drop=True)

df['sound1'] = df['sound1'].apply(lambda x: r'' + x)
df['sound2'] = df['sound2'].apply(lambda x: r'' + x)

def extract_desired_portion(filename):
    # Split the filename using the backslash as the separator
    split_filename = filename.split('\\')

    # Get the last element from the split_filename list, which contains the desired portion
    desired_portion = split_filename[-1]

    # Remove the file extension from the desired portion
    desired_portion = desired_portion.replace('.wav', '')

    return desired_portion


df['sound1'] = df['sound1'].apply(lambda x: extract_desired_portion(x))
df['sound2'] = df['sound2'].apply(lambda x: extract_desired_portion(x))

df = df.rename(columns={'slider.response': 'slider_response'})


df


# %%

#%%
# Save the subset DataFrame to a new CSV file with the provided name
csv_file_path = f"C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/{output_file_name}.csv"
df.to_csv(csv_file_path, index=False)
