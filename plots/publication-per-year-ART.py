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
y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
x_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y1 = np.array([2, 2, 0, 3, 7, 4, 5, 6, 12, 10, 13, 11, 6, 11, 12, 9, 11, 15, 20, 8])

x_data22 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])  # without 2024
x_data2 = np.array([ 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])  # without 2024
y2 = np.array([2, 2, 0, 3, 7, 4, 5, 6, 12, 10, 13, 11, 6, 11, 12, 9, 11, 15, 20])

# Make a data definition
X_axis = np.arange(len(x))

fig, ax = plt.subplots()

# Setting the x-axis to 0-5
# and y-axis to 1-15
plt.axis([-1, 19.5, 0, 19])
plt.grid(axis='y')

# Multiple colors of bars
# p1 = ax.bar(range(len(y1)), y1, label = '$DBT$', color='0.2') 
p1 = ax.bar(X_axis, y1,  
        label = '$DBT$')
# p2 = ax.bar(X_axis, y2, width=0.2, 
#         label = '$DBT$ \\ $DBT_{ART}$', color='0.5')
# p3 = ax.bar(X_axis +0.2, y3, width=0.2, 
#         label = '$DBT_{ART}$', color='0.8')

#calculate equation for trendline
#plt.plot(x, y1, '-o', color='orange')

(m,b) = np.polyfit(x_data2 , y2, 1)
yp = np.polyval([m,b],x_data2)
equation = 'y = ' + str(round(m,4)) + 'x ' + str(round(b,4))
p2 = ax.plot(x_data2,yp)
p3 = ax.text(0.2, 0.57,equation, fontsize=12, fontstyle='italic', horizontalalignment='center',
     verticalalignment='center',
     transform=ax.transAxes)

z0 = np.polyfit(x_data22 , y2, 1)
pt0 = np.poly1d(z0)
# z1 = np.polyfit(x_data , y2, 1)
# pt1 = np.poly1d(z1)
# z2 = np.polyfit(x_data , y3, 1)
# pt2 = np.poly1d(z2)

# Xticks
plt.xticks(X_axis, x)
plt.yticks(y)

#add trendline to plot
p4, = ax.plot(x_data22, pt0(x_data22), label = '$DBT$', color="0.2", linestyle="solid")
# p5, = ax.plot(x_data, pt1(x_data), label = '$DBT$ \\ $DBT_{ART}$', color="0.5", linestyle="dotted")
# p6, = ax.plot(x_data, pt2(x_data), label = '$DBT_{ART}$', color="0.8", linestyle=(0, (3, 1, 1, 1)))


# Display the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
#plt.savefig('test.jpg', bbox_inches='tight')


# # Make a data definition
# _data = {'ART': y1,
#         'DBT/ART': y2}
# _df = pd.DataFrame(_data,columns=['ART', 'DBT/ART'], index = x)

# # Multiple bar chart
# _df.plot.bar()

# # Display the plot
# plot.show()




# plt.bar(x, y1, color='0.7')
# plt.bar(x, y2, bottom=y1, color='0.2')

# plot bars in stack manner
# plt.bar(x, y1, width=0.2, color='0.7', align='center')
# plt.bar(x+0.2, y2, width=0.2, color='0.2', align='center')
# plt.xlabel("Year")
# plt.ylabel("Number of papers")
# # plt.legend(["ART", "Others"])
# #plt.title("Scores by Teams in 4 Rounds")
# plt.show()