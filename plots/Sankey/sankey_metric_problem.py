import matplotlib
import pandas as pd
from pysankey import sankey
import matplotlib.pyplot as plt

colorDict = {
    'Test data generation':'0.1',
    'Test case prioritisation':'0.1',
    'Test case selection':'0.1',
    'Test suite evaluation':'0.1',
    'Test suite reduction':'0.1',
    'Fault localisation':'0.1',
    'Other':'0.1',
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
    '/home/islam/MyWork/Code/PlotGeneration/Survey/metric-problem.csv', sep=',',
    names=['id', 'Metric', 'Problem', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['Metric'].values[1:], right=df['Problem'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=20, fontsize=13
)
# plt.rcParams["figure.figsize"] = (20,30)
plt.tight_layout()
# plt.show() # to display
plt.savefig('metric-problem.pdf', bbox_inches='tight') # to save