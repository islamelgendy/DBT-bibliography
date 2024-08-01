import pandas as pd
from pysankey import sankey
import matplotlib.pyplot as plt

colorDict = {
    'Stand-Alone':'magenta',
    'Model-Based':'blue',
    'Web':'darkgray',
    'Neural networks':'coral',
    'GUI Apps':'gold',
    'Other':'indigo',
    'Test data generation':'0.1',
    'Test case prioritisation':'0.1',
    'Test case selection':'0.1',
    'Test suite evaluation':'0.1',
    'Test suite reduction':'0.1',
    'Fault localisation':'0.1',
    'Other':'0.1'
}

df = pd.read_csv(
    '/home/islam/MyWork/Code/PlotGeneration/Survey/problem-application.csv', sep=',',
    names=['id', 'Problem', 'Application', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['Application'].values[1:], right=df['Problem'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=30, fontsize=13
)

plt.tight_layout()

plt.savefig('problem-subjects.pdf', bbox_inches='tight') # to save
