#!/usr/bin/env python3

# load the dataset
import os

import matplotlib as plt
import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Computing data

housedata = pd.read_csv(filepath_or_buffer='/.../class5-homework/housing.data.txt',
                        sep = ',',
                        header = 0)
print(housedata)


# Compute and print summary statistics


housedata = pd.read_csv(filepath_or_buffer = '/.../class5_homework/housing.data.txt',
                        sep = ',',
                        header = 0)

# Create a DataFrame
pd.DataFrame(housedata)
print(housedata.describe())


# Visualize

pretty_print('housedata Dataframe',housedata.to_string())
pretty_print('housedata columns',housedata.columns)

os.makedirs('plots',exist_ok= True)

# Plotting line chart
plt.plot(housedata['medv'], color='red')
plt.title('medv by indus')
plt.xlabel('indus')
plt.ylabel('medv')
plt.savefig(f'plots/medv_by_indus_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(housedata['age'], bins=3, color='g')
plt.title('age')
plt.xlabel('age')
plt.ylabel('Count')
plt.savefig(f'plots/age_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(housedata['crim'], housedata['ptratto'], color='red')
plt.title('crim by ptratto')
plt.xlabel('crim')
plt.ylabel('ptratto')
plt.savefig(f'plots/crime_by_ptratto.png', format='png')
plt.close()