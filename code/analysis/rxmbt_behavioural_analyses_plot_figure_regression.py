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

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', and 'participants'

# Group the data by 'participants'
grouped = df.groupby('Code')

# Create a scatter plot for each group
for participant, group in grouped:
    plt.scatter(group['QA'], group['mean_10Hz'], label=participant, color='b')

# Adding labels and title
plt.xlabel('QA')
plt.ylabel('Mean_10Hz')
plt.title('Scatter Plot')


# Displaying the plot
plt.show()




#%% ADD R

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', and 'Code'

# Group the data by 'Code'
grouped = df.groupby('Code')

# Create a scatter plot for each group
for participant, group in grouped:
    plt.scatter(group['QA'], group['mean_10Hz'], label=participant)

# Combine all data points
combined_data = pd.concat([group[['QA', 'mean_10Hz']] for _, group in grouped])

# Perform polynomial regression
degree = 1  # Adjust the degree of the polynomial as needed
coeffs = np.polyfit(combined_data['QA'], combined_data['mean_10Hz'], degree)
poly = np.poly1d(coeffs)
x_vals = np.linspace(combined_data['QA'].min(), combined_data['QA'].max(), 100)
y_vals = poly(x_vals)

# Calculate Pearson correlation coefficient
correlation_coefficient, _ = pearsonr(combined_data['QA'], combined_data['mean_10Hz'])

# Plot the smoothed regression line with the correlation coefficient as a label
reg = plt.plot(x_vals, y_vals, color='r', label=f'Smoothed Regression Line (r={correlation_coefficient:.2f})')


ax = plt.gca()
ax.legend(handles = [reg[0]])

# Adding labels and title
plt.xlabel('QA')
plt.ylabel('mean_10Hz')
plt.title('Scatter Plot with Smoothed Regression Line')


# Displaying the plot
plt.show()


#%% MULTPLE PLOTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', 'Code', and other columns of interest

# Get the columns of interest
columns_of_interest = ['mean_10Hz','mean_20Hz','mean_30Hz','mean_40Hz','mean_60Hz','mean_80Hz','mean_90Hz']  # Add other column names of interest here

# Iterate over each column of interest
for column in columns_of_interest:
    # Create a scatter plot for each participant
    plt.figure()
    
    # Group the data by 'Code'
    grouped = df.groupby('Code')
    
    # Iterate over each participant and plot the scatter plot and regression line
    for participant, group in grouped:
        plt.scatter(group['QA'], group[column], label=participant)
        
        # Perform polynomial regression
        degree = 1  # Adjust the degree of the polynomial as needed
        coeffs = np.polyfit(group['QA'], group[column], degree)
        poly = np.poly1d(coeffs)
        x_vals = np.linspace(group['QA'].min(), group['QA'].max(), 100)
        y_vals = poly(x_vals)
    
        # Calculate Pearson correlation coefficient
        #correlation_coefficient, _ = pearsonr(group['QA'], group[column])
    
        # Plot the smoothed regression line with the correlation coefficient as a label
        plt.plot(x_vals, y_vals, color='r', label='Smoothed Regression Line (r=')
    
    # Adding labels and title
    plt.xlabel('QA')
    plt.ylabel(column)
    plt.title(f'Scatter Plot of {column} with Regression Line')
    
    


#%% TEST MULTIPLE Good 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', 'Code', and other columns of interest

# Get the columns of interest
columns_of_interest = ['mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']

# Calculate the number of rows and columns for the subplots
n_rows = 4
n_cols = int(np.ceil(len(columns_of_interest) / n_rows))

# Create a figure with subplots
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(12, 16))
fig.tight_layout(pad=3.0)

# Iterate over each column of interest
for i, column in enumerate(columns_of_interest):
    # Calculate the row and column indices for the subplot
    row_idx = i // n_cols
    col_idx = i % n_cols
    
    # Get the corresponding subplot axis
    ax = axes[row_idx, col_idx]
    
    # Group the data by 'Code'
    grouped = df.groupby('Code')
    
    # Iterate over each participant and plot the scatter plot and regression line
    for participant, group in grouped:
        ax.scatter(group['QA'], group[column], color='b', s=5 , label=participant)
        
    # Perform linear regression
    degree = 1  # Adjust the degree of the polynomial as needed
    coeffs = np.polyfit(group['QA'], group[column], degree)
    poly = np.poly1d(coeffs)
    x_vals = np.linspace(group['QA'].min(), group['QA'].max(), 100)
    y_vals = poly(x_vals)
        
        # Plot the regression line
    ax.plot(x_vals, y_vals, color='r')
    
    # Calculate Pearson correlation coefficient
    correlation_coefficient, _ = pearsonr(df['QA'], df[column])
    
    # Plot the smoothed regression line with the correlation coefficient as a label
    reg = plt.plot(x_vals, y_vals, color='r', label=f'Smoothed Regression Line (r={correlation_coefficient:.2f})')


    # Add the correlation coefficient as a label
    ax.set_title(f'{column} (r={correlation_coefficient:.2f})')
    ax.set_xlabel('QA')
    ax.set_ylabel(column)



# Display the plot
plt.show()


#%% TEST NO BASELINE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', 'Code', and other columns of interest

# Get the columns of interest
columns_of_interest = ['mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']

# Calculate the number of rows and columns for the subplots
n_rows = 4
n_cols = int(np.ceil(len(columns_of_interest) / n_rows))

# Create a figure with subplots
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(12, 16))
fig.tight_layout(pad=3.0)

# Iterate over each column of interest
for i, column in enumerate(columns_of_interest):
    # Calculate the row and column indices for the subplot
    row_idx = i // n_cols
    col_idx = i % n_cols
    
    # Get the corresponding subplot axis
    ax = axes[row_idx, col_idx]
    
    # Group the data by 'Code'
    grouped = df.groupby('Code')
    
    # Collect the data for all participants
    all_x = []
    all_y = []
    
    for participant, group in grouped:
        ax.scatter(group['STAI-T'], group[column], color='b', s=5, label=participant)
        
        # Collect data for regression line
        all_x.extend(group['STAI-T'])
        all_y.extend(group[column])
    
    # Perform linear regression for all participants
    coeffs = np.polyfit(all_x, all_y, 1)
    poly = np.poly1d(coeffs)
    x_vals = np.linspace(min(all_x), max(all_x), 100)
    y_vals = poly(x_vals)
    
    # Plot the regression line for all participants
    ax.plot(x_vals, y_vals, color='black', label='Regression Line')
    
    # Calculate Pearson correlation coefficient
    correlation_coefficient, _ = pearsonr(all_x, all_y)
    
    # Add the correlation coefficient as a label
    ax.set_title(f'{column} (r={correlation_coefficient:.2f})')
    ax.set_xlabel('STAI-T')
    ax.set_ylabel(column)

    # Add legend to each subplot
   

# Display the plot
plt.show()


#%%TEST BASELINE MULTI


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assuming you have a DataFrame named 'df' with columns 'QA', 'Mean_10Hz', 'Code', and other columns of interest

# Get the columns of interest
columns_of_interest = ['mean_10Hz', 'mean_20Hz', 'mean_30Hz', 'mean_40Hz', 'mean_60Hz', 'mean_80Hz', 'mean_90Hz']

# Calculate the number of rows and columns for the subplots
n_rows = 4
n_cols = int(np.ceil(len(columns_of_interest) / n_rows))

# Create a figure with subplots
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(12, 16))
fig.tight_layout(pad=3.0)

# Iterate over each column of interest
for i, column in enumerate(columns_of_interest):
    # Calculate the row and column indices for the subplot
    row_idx = i // n_cols
    col_idx = i % n_cols
    
    # Get the corresponding subplot axis
    ax = axes[row_idx, col_idx]
    
    # Group the data by 'Code'
    grouped = df.groupby('Code')
    
    # Collect the data for all participants
    all_x = []
    all_y = []
    
    for participant, group in grouped:
        # Calculate the mean of the column
        overall_mean = df[column].mean()
        
        # Baseline each point with the overall mean
        baseline_y = group[column] - overall_mean
        
        ax.scatter(group['STAI-T'], baseline_y, color='b', s=5, label=participant)
        
        # Collect data for regression line
        all_x.extend(group['STAI-T'])
        all_y.extend(baseline_y)
    
    # Perform linear regression for all participants
    coeffs = np.polyfit(all_x, all_y, 1)
    poly = np.poly1d(coeffs)
    x_vals = np.linspace(min(all_x), max(all_x), 100)
    y_vals = poly(x_vals)
    
    # Plot the regression line for all participants
    ax.plot(x_vals, y_vals, color='black', label='Regression Line')
    
    # Calculate Pearson correlation coefficient
    correlation_coefficient, _ = pearsonr(all_x, all_y)
    
    # Add the correlation coefficient as a label
    ax.set_title(f'{column} (r={correlation_coefficient:.2f})')
    ax.set_xlabel('STAI-T')
    ax.set_ylabel(f'{column} (baseline)')
    
    # Add legend to each subplot
    

# Display the plot
plt.show()





#%%
df_cond1 = df[df['QA_split'] == 1]

df_cond2 = df[df['QA_split'] == 2]


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

#%%


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
