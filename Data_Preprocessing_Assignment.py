#!/usr/bin/env python
# coding: utf-8

# In[81]:


# Import required packages.
import pandas as pd
import matplotlib.pyplot as plt

# Creates necessary function: see Docstrings. 
def to_data_frame(filename, summary = False):
    """
    Creates a data frame for the given file (.gct) and
    prints the number of rows and columns (if summary is True)
    
    Parameters:
    filename (.gct): The file to convert.
    summary (boolean): True/False value if row and column
    size should be printed.
    
    Returns:
    dataframe: the converted file.
    """
    # Read the file in through read_csv, using tabs instead of commas.
    # Skips first 2 rows.
    df = pd.read_csv(filename, sep='\t', skiprows=2)
    
    # Turns the name and description column into index.
    df.set_index(["Name", "Description"], inplace=True)
    
    # If summary is True, then prints out number of rows and columns.
    if summary == True:
        row, col = df.shape
        print(f"Rows: {row}")
        print(f"Columns: {col}")
        
    # Returns the data frame.
    return df

# Sets function1 and function2 to given datasets.
function1 = "BRCA_minimal_60x19.gct"
function2 = "BRCA_large_20783x40.gct"

# Calls to_data_frame, first with # of columns and rows, and then without.
func_1_df = to_data_frame(function1, True)
func_2_df = to_data_frame(function2)

# Plots histograms with their respective titles
for i in ["A7-A0DB-normal", "A7-A13E-normal", "BH-A0B3-primary", "BH-A0B5-primary"]:
    plt.figure()
    df_2_plot = plt.hist(func_2_df[i], bins = 500)
    plt.xlim(0,50000)
    plt.title(f"Histogram of {i}")

# Turns the samples into rows.
summary_df = func_2_df.describe().T 

# Calculates the rows to be the mean, median, and standard deviation.
summary_df = summary_df[['mean', '50%', 'std']]

# Renames the 50% to be named "median".
summary_df.rename(columns={'50%': 'median'}, inplace=True)
print(summary_df)

# Filters rows from #2b whose maximum value is < 1000.
filtered_df = func_2_df.loc[func_2_df.max(axis=1) >= 1000]

# Finds the mean and median of the columns.
filtered_mean = filtered_df.mean()
filtered_median = filtered_df.median()

# Prints the means and medians. 
print(f"Mean of each column after filtering: \n{filtered_mean}")
print(f"Median of each column after filtering: \n{filtered_median}")

# Plots histograms with their respective titles
for i in ["A7-A0DB-normal", "A7-A13E-normal", "BH-A0B3-primary", "BH-A0B5-primary"]:
    plt.figure()
    df_2_plot = plt.hist(filtered_df[i], bins = 500)
    plt.xlim(0,50000)
    plt.title(f"Histogram of {i} - transformed")

# In[ ]:




