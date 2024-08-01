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
    '/home/islam/MyWork/Code/PlotGeneration/Survey/artefact-application.csv', sep=',',
    names=['id', 'Artefact', 'Application', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['Application'].values[1:], right=df['Artefact'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=30, fontsize=13
)

plt.tight_layout()
# plt.show() # to display
plt.savefig('artefact-subjects.pdf', bbox_inches='tight') # to save
