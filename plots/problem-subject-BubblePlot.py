import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

df = pd.read_csv(
    '/home/islam/MyWork/Code/PlotGeneration/Survey/problem-application.csv', sep=',',
    names=['id', 'Problem', 'Application', 'count']	
)

x = df['Application'].tolist()[1:]
y = df['Problem'].tolist()[1:]
z = df['count'].tolist()[1:]
sizes = [(eval(i)+1)*20 for i in z]

# Encode the categories as integers
category_codes, category_names = pd.factorize(df['count'][1:])

# Initiate the chart
fig, ax = plt.subplots(figsize=(7,5), dpi=200)

scatter = ax.scatter(x, 
                     y, 
                     s=sizes, 
                     c=category_codes,
                     cmap="viridis",
                     alpha=0.6)

#label each bubble
for n,c,r in zip(x,y,z):
    plt.annotate("{}".format(r),xy=(n, c), ha="center", va="center")
    
# Legend
from matplotlib.patches import Patch
handles = [Patch(facecolor=scatter.cmap(scatter.norm(i)), label=label)
           for i, label in enumerate(category_names)]

# Shrink current axis by 20%
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# ax.legend(handles=handles, title='Counts', loc='center left', bbox_to_anchor=(1, 0.5))

# Custom axes and display chart
ax.set_xlabel('Subject domains')
ax.set_ylabel('Problems')
# plt.xlabel("Applications")
# plt.ylabel("Problems")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("problem-application-bubblePlot.jpg")
plt.show()