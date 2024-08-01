import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


x_data22 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])  # without 2024
x_data2 = np.array([ 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])  # without 2024

data = [ 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 1, 3, 2, 2, 6, 1, 2]
y =    [ 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 1, 3, 2, 2, 6, 1]
labels = [ '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']

fig, ax = plt.subplots()

plt.axis([-1, 19.5, 0, 6])
plt.xticks(range(len(data)), labels)
plt.xlabel('Year')
plt.ylabel('Number of Tools')
plt.grid(axis='y')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
#plt.title('I am title')
ax.bar(range(len(data)), data) 

(m,b) = np.polyfit(x_data2 , y, 1)
yp = np.polyval([m,b],x_data2)
equation = 'y = ' + str(round(m,4)) + 'x ' + str(round(b,4))
p2 = ax.plot(x_data2,yp)
p3 = ax.text(0.2, 0.7,equation, fontsize=12, fontstyle='italic', horizontalalignment='center',
     verticalalignment='center',
     transform=ax.transAxes)

z0 = np.polyfit(x_data22 , y, 1)
pt0 = np.poly1d(z0)

p4, = ax.plot(x_data22, pt0(x_data22), label = '$DBT$', color="0.2", linestyle="solid")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()