import pandas as pd
from pysankey import sankey
import matplotlib.pyplot as plt

colorDict = {
    'Stand-Alone':'0.1',
    'Model-Based':'0.1',
    'Web':'0.1',
    'Neural networks':'0.1',
    'GUI Apps':'0.1',
    'Other':'0.1',
    # 'Mobile':'0.1',
    # 'Database':'0.1',
    # 'Euclidean':'0.8',
    # 'Jaccard':'0.7',
    # 'Edit':'0.6',
    # 'Hamming':'0.5',
    # 'Manhattan':'0.4',
    # 'OtherG':'0.3',
    # 'Specialised':'0.2'
    'Euclidean':'magenta',
    'Jaccard':'blue',
    'Levenshtein':'darkgray',
    'Hamming':'coral',
    'Manhattan':'gold',
    'Other Generic':'darkcyan',
    'Specialised':'crimson'
}

df = pd.read_csv(
    '/home/islam/MyWork/Code/PlotGeneration/Survey/metric-application.csv', sep=',',
    names=['id', 'Metric', 'Application', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['Metric'].values[1:], right=df['Application'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=30, fontsize=17
)

plt.tight_layout()
# plt.show() # to display
plt.savefig('metric-subjects.pdf', bbox_inches='tight') # to save
