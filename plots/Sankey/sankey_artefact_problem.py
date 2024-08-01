import pandas as pd
from pysankey import sankey
import matplotlib.pyplot as plt

colorDict = {
    'Test data generation':'magenta',
    'Test case prioritisation':'blue',
    'Test case selection':'darkgray',
    'Test suite evaluation':'coral',
    'Test suite reduction':'gold',
    'Fault localisation':'darkcyan',
    'Other':'crimson',
    'Input':'0.1',
    'Test Script':'0.1',
    'Hybrid':'0.1',
    'Execution':'0.1',
    'Transitions':'0.1',
    'Coverage':'0.1',
    'Feature':'0.1',
    'Output':'0.1',
    'GUI':'0.1',
    'Other':'0.1'
}

df = pd.read_csv(
    '/home/islam/MyWork/Code/PlotGeneration/Survey/artefact-problem.csv', sep=',',
    names=['id', 'Artefact', 'Problem', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['Problem'].values[1:], right=df['Artefact'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=30, fontsize=13
)

plt.tight_layout()
# plt.show() # to display
plt.savefig('artefact-problems.pdf', bbox_inches='tight') # to save
