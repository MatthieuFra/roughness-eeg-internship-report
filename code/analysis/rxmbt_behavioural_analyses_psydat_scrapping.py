# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

from psychopy.misc import fromFile

# Specify the path to the log file
fpath = "C:/Users/mfratice/OneDrive - Institut Pasteur Paris/roughxpmbt/01_roughxpmbt_data/00_roughxpmbt_psychopy/roughxpmbt_2023-05-09_14h31.26.147_CJ20230509_run2/roughxpmbt_2023-05-09_14h31.26.147_CJ20230509_run2.psydat"
output_file_name = "GCYIJW"


# TO SCRAP THE DATAS


# (replace with the file path to your .psydat file)
list = []
psydata = fromFile(fpath)
for entry in psydata.entries:
    list.append(entry)

#%%
# list dict 

len(list)

#%%
# Save the subset DataFrame to a new CSV file with the provided name
csv_file_path = f"C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_questionnaires/{output_file_name}.csv"
aligned_df.to_csv(csv_file_path, index=False)
# %%
