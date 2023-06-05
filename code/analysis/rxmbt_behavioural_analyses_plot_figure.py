# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import glob
import os

% matplotlib widget
#%% To do that accross all the participants

# sd for the figure 

# Read the CSV file
df = pd.read_csv('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/all_participants.csv')

df

# %%

df_cond1 = df[df['QA_split'] == 1]

df_cond2 = df[df['QA_split'] == 2]

subset_df = df[['Code', 'mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']]

subset_df = subset_df.rename(columns={'mean_10Hz': '10'})
subset_df = subset_df.rename(columns={'mean_20Hz': '20'})
subset_df = subset_df.rename(columns={'mean_30Hz': '30'})
subset_df = subset_df.rename(columns={'mean_40Hz': '40'})
subset_df = subset_df.rename(columns={'mean_60Hz': '60'})
subset_df = subset_df.rename(columns={'mean_80Hz': '80'})
subset_df = subset_df.rename(columns={'mean_90Hz': '90'})

subset_df1 = df_cond1[['Code', 'mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']]

subset_df1 = subset_df1.rename(columns={'mean_10Hz': '10'})
subset_df1 = subset_df1.rename(columns={'mean_20Hz': '20'})
subset_df1 = subset_df1.rename(columns={'mean_30Hz': '30'})
subset_df1 = subset_df1.rename(columns={'mean_40Hz': '40'})
subset_df1 = subset_df1.rename(columns={'mean_60Hz': '60'})
subset_df1 = subset_df1.rename(columns={'mean_80Hz': '80'})
subset_df1 = subset_df1.rename(columns={'mean_90Hz': '90'})

subset_df2 = df_cond2[['Code', 'mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']]

subset_df2 = subset_df2.rename(columns={'mean_10Hz': '10'})
subset_df2 = subset_df2.rename(columns={'mean_20Hz': '20'})
subset_df2 = subset_df2.rename(columns={'mean_30Hz': '30'})
subset_df2 = subset_df2.rename(columns={'mean_40Hz': '40'})
subset_df2 = subset_df2.rename(columns={'mean_60Hz': '60'})
subset_df2 = subset_df2.rename(columns={'mean_80Hz': '80'})
subset_df2 = subset_df2.rename(columns={'mean_90Hz': '90'})

#subset_df

#%%
# Plotting settings
participant_opacity = 0.1
participant_linewidth = 1.0



# %% SIMPLE PLOT
from scipy.interpolate import make_interp_spline

# Extract the column names for x-axis values
x_columns = subset_df.columns[1:]

# Convert the column names to corresponding numeric values
x_values = np.arange(1, len(x_columns) + 1)

# Calculate the mean across the rows for each column
mean_values = subset_df.drop('Code', axis=1).mean()

# Calculate the overall mean
overall_mean = mean_values.mean()

# Iterate over the rows of the DataFrame
for index, row in subset_df.iterrows():
    participant = row['Code']
    data = row.drop('Code')  # Exclude the 'Code' column from the data
    
    print(data)

    participant_mean_values = data.mean()

    print(participant_mean_values)
    # Subtract the mean value of the participant from the data

    data = data - participant_mean_values
    
    # Smooth the data using a spline interpolation
    x_smooth = np.linspace(x_values.min(), x_values.max(), 100)
    spline = make_interp_spline(x_values, data, k=3)
    smoothed_data = spline(x_smooth)
    
    # Plot the data for the current participant with modified opacity and linewidth
    plt.plot(x_smooth, smoothed_data, label=participant, color='r', linestyle='--',  alpha=participant_opacity, linewidth=participant_linewidth)

    # Add points for the values in the data with modified size
    plt.scatter(x_values, data, color='black', marker='o', s=0.5)

# Subtract the overall mean value from the mean curve data
mean_values -= overall_mean

# Smooth the mean curve using a spline interpolation
mean_smooth = make_interp_spline(x_values, mean_values, k=3)
mean_smooth_data = mean_smooth(x_smooth)

# Plot the mean curve with smoothing
low_autism = plt.plot(x_smooth, mean_smooth_data, color='black', linestyle='solid', linewidth=2, label='low QA')


plt.axhline(y=0, linestyle='--', color='gray', linewidth=0.5)

# Set x-axis tick labels to column names
plt.xticks(x_values, x_columns)

# Add labels and legend
plt.xlabel('Freq')
plt.ylabel('Aversion')

# Show the plot
plt.show()






# %% FISRT NO BASELINE

from scipy.interpolate import make_interp_spline

subset_df = subset_df1

# Extract the column names for x-axis values
x_columns = subset_df.columns[1:]

# Convert the column names to corresponding numeric values
x_values = np.arange(1, len(x_columns) + 1)

# Calculate the mean across the rows for each column
mean_values = subset_df.drop('Code', axis=1).mean()

# Iterate over the rows of the DataFrame
for index, row in subset_df.iterrows():
    participant = row['Code']
    data = row.drop('Code')  # Exclude the 'Code' column from the data
    
    # Smooth the data using a spline interpolation
    x_smooth = np.linspace(x_values.min(), x_values.max(), 100)
    spline = make_interp_spline(x_values, data, k=3)
    smoothed_data = spline(x_smooth)
    
    # Plot the data for the current participant with modified opacity and linewidth
    plt.plot(x_smooth, smoothed_data, label=participant, color='b', linestyle='--',  alpha=participant_opacity, linewidth=participant_linewidth)


    # Add points for the values in the data
    plt.scatter(x_values, data, color='black', marker='o', s=0.5)

# Smooth the mean curve using a spline interpolation
mean_smooth = make_interp_spline(x_values, mean_values, k=3)
mean_smooth_data = mean_smooth(x_smooth)

# Plot the mean curve with smoothing
low_autism = plt.plot(x_smooth, mean_smooth_data, color='blue', linestyle='solid', linewidth=2, label='low QA')





subset_df = subset_df2

# Extract the column names for x-axis values
x_columns = subset_df.columns[1:]

# Convert the column names to corresponding numeric values
x_values = np.arange(1, len(x_columns) + 1)

# Calculate the mean across the rows for each column
mean_values = subset_df.drop('Code', axis=1).mean()

# Iterate over the rows of the DataFrame
for index, row in subset_df.iterrows():
    participant = row['Code']
    data = row.drop('Code')  # Exclude the 'Code' column from the data
    
    # Smooth the data using a spline interpolation
    x_smooth = np.linspace(x_values.min(), x_values.max(), 100)
    spline = make_interp_spline(x_values, data, k=3)
    smoothed_data = spline(x_smooth)
    
    # Plot the data for the current participant with modified opacity and linewidth
    plt.plot(x_smooth, smoothed_data, label=participant, color='r', linestyle='--',  alpha=participant_opacity, linewidth=participant_linewidth)


    # Add points for the values in the data
    plt.scatter(x_values, data, color='black', marker='o', s=0.5)

# Smooth the mean curve using a spline interpolation
mean_smooth = make_interp_spline(x_values, mean_values, k=3)
mean_smooth_data = mean_smooth(x_smooth)

# Plot the mean curve with smoothing
high_autism = plt.plot(x_smooth, mean_smooth_data, color='red', linestyle='solid', linewidth=2, label='high QA')


ax = plt.gca()
ax.legend(handles = [low_autism[0], high_autism[0]])

# Set x-axis tick labels to column names
plt.xticks(x_values, x_columns)

# Add labels and legend
plt.xlabel('Freq')
plt.ylabel('Aversion')

# Show the plot
plt.show()







# %% BASELINE
from scipy.interpolate import make_interp_spline

subset_df = subset_df1

# Extract the column names for x-axis values
x_columns = subset_df.columns[1:]

# Convert the column names to corresponding numeric values
x_values = np.arange(1, len(x_columns) + 1)

# Calculate the mean across the rows for each column
mean_values = subset_df.drop('Code', axis=1).mean()

# Calculate the overall mean
overall_mean = mean_values.mean()

# Iterate over the rows of the DataFrame
for index, row in subset_df.iterrows():
    participant = row['Code']
    data = row.drop('Code')  # Exclude the 'Code' column from the data
    
    print(data)

    participant_mean_values = data.mean()

    print(participant_mean_values)
    # Subtract the mean value of the participant from the data

    data = data - participant_mean_values
    
    # Smooth the data using a spline interpolation
    x_smooth = np.linspace(x_values.min(), x_values.max(), 100)
    spline = make_interp_spline(x_values, data, k=3)
    smoothed_data = spline(x_smooth)
    
    # Plot the data for the current participant with modified opacity and linewidth
    plt.plot(x_smooth, smoothed_data, label=participant, color='b', linestyle='--',  alpha=participant_opacity, linewidth=participant_linewidth)

    # Add points for the values in the data with modified size
    plt.scatter(x_values, data, color='black', marker='o', s=0.5)

# Subtract the overall mean value from the mean curve data
mean_values -= overall_mean

# Smooth the mean curve using a spline interpolation
mean_smooth = make_interp_spline(x_values, mean_values, k=3)
mean_smooth_data = mean_smooth(x_smooth)

# Plot the mean curve with smoothing
low_autism = plt.plot(x_smooth, mean_smooth_data, color='blue', linestyle='solid', linewidth=2, label='low QA')







subset_df = subset_df2

# Extract the column names for x-axis values
x_columns = subset_df.columns[1:]

# Convert the column names to corresponding numeric values
x_values = np.arange(1, len(x_columns) + 1)

# Calculate the mean across the rows for each column
mean_values = subset_df.drop('Code', axis=1).mean()

# Calculate the overall mean
overall_mean = mean_values.mean()

# Iterate over the rows of the DataFrame
for index, row in subset_df.iterrows():
    participant = row['Code']
    data = row.drop('Code')  # Exclude the 'Code' column from the data
    
    print(data)

    participant_mean_values = data.mean()

    print(participant_mean_values)
    # Subtract the mean value of the participant from the data

    data = data - participant_mean_values
    
    # Smooth the data using a spline interpolation
    x_smooth = np.linspace(x_values.min(), x_values.max(), 100)
    spline = make_interp_spline(x_values, data, k=3)
    smoothed_data = spline(x_smooth)
    
    # Plot the data for the current participant with modified opacity and linewidth
    plt.plot(x_smooth, smoothed_data, label=participant, color='r', linestyle='--',  alpha=participant_opacity, linewidth=participant_linewidth)

    # Add points for the values in the data with modified size
    plt.scatter(x_values, data, color='black', marker='o', s=0.5)

# Subtract the overall mean value from the mean curve data
mean_values -= overall_mean

# Smooth the mean curve using a spline interpolation
mean_smooth = make_interp_spline(x_values, mean_values, k=3)
mean_smooth_data = mean_smooth(x_smooth)

# Plot the mean curve with smoothing
high_autism = plt.plot(x_smooth, mean_smooth_data, color='red', linestyle='solid', linewidth=2, label='high QA')











ax = plt.gca()
ax.legend(handles = [low_autism[0], high_autism[0]])



plt.axhline(y=0, linestyle='--', color='gray', linewidth=0.5)

# Set x-axis tick labels to column names
plt.xticks(x_values, x_columns)

# Add labels and legend
plt.xlabel('Freq')
plt.ylabel('Aversion')

# Show the plot
plt.show()





# %%
