# %%
# this script is used to preprocess the data into a usable mne epoch object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import glob
import os

% matplotlib widget



#%% SIMPLE PLOT WITH R

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

column_freq = 'mean_90Hz'

# Group the data by 'Code'
grouped = df.groupby('Code')

# Create a scatter plot for each group
for participant, group in grouped:
    plt.scatter(group['QA'], group[column_freq], label=participant, color='b', s=5)

# Combine all data points
combined_data = pd.concat([group[['QA', column_freq]] for _, group in grouped])

# Perform polynomial regression
degree = 1  # Adjust the degree of the polynomial as needed
coeffs = np.polyfit(combined_data['QA'], combined_data[column_freq], degree)
poly = np.poly1d(coeffs)
x_vals = np.linspace(combined_data['QA'].min(), combined_data['QA'].max(), 100)
y_vals = poly(x_vals)

# Calculate Pearson correlation coefficient
correlation_coefficient, _ = pearsonr(combined_data['QA'], combined_data[column_freq])

# Plot the smoothed regression line with the correlation coefficient as a label
reg = plt.plot(x_vals, y_vals, color='r', label=f'Smoothed Regression Line (r={correlation_coefficient:.2f})')


ax = plt.gca()
ax.legend(handles = [reg[0]])

# Adding labels and title
plt.xlabel('QA')
plt.ylabel(column_freq)
plt.title('Scatter Plot with Smoothed Regression Line')


# Displaying the plot
plt.show()


#%% Multi NO BASELINE
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
        ax.scatter(group['QA'], group[column], color='b', s=5, label=participant)
        
        # Collect data for regression line
        all_x.extend(group['QA'])
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
    ax.set_xlabel('QA')
    ax.set_ylabel(column)

    # Add legend to each subplot
   

# Display the plot
plt.show()


#%%Multi BASELINE


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
        
        ax.scatter(group['QA'], baseline_y, color='b', s=5, label=participant)
        
        # Collect data for regression line
        all_x.extend(group['QA'])
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
    ax.set_xlabel('QA')
    ax.set_ylabel(f'{column} (baseline)')
    
    # Add legend to each subplot
    

# Display the plot
plt.show()




# %%
