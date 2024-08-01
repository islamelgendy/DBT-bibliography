# importing package
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
import numpy as np
import pandas as pd

# Define linestyles
linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or ':'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

# create data
# y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
x = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
x_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y1 = np.array([2, 4, 4, 7, 14, 18, 23, 29, 41, 51, 64, 75, 81, 92, 104, 113, 125, 139, 159, 167])
               

# Make a data definition
X_axis = np.arange(len(x))

fig, ax = plt.subplots()

# Setting the x-axis to 0-5
# and y-axis to 1-15
plt.axis([-1, 19.5, 0, 180])
plt.grid(axis='y')

# Multiple colors of bars
# p1 = ax.bar(range(len(y1)), y1, label = '$DBT$', color='0.2') 
p1 = ax.bar(X_axis, y1,  
        label = '$DBT$')

# Xticks
plt.xticks(X_axis, x)
# plt.yticks(y)


# Display the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
#plt.savefig('test.jpg', bbox_inches='tight')
