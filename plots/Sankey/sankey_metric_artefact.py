import pandas as pd
from pysankey import sankey
import matplotlib.pyplot as plt

colorDict = {
    'Input':'0.1',
    'Test Script':'0.1',
    'Hybrid':'0.1',
    'Execution':'0.1',
    'Transitions':'0.1',
    'Coverage':'0.1',
    'Feature':'0.1',
    'Output':'0.1',
    'GUI':'0.1',
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
    '/home/islam/MyWork/Code/PlotGeneration/Survey/metric-artefact.csv', sep=',',
    names=['id', 'metric', 'artefact', 'count']	
)
weight = df['count'].values[1:].astype(float)

ax = sankey(
      left=df['metric'].values[1:], right=df['artefact'].values[1:],  colorDict=colorDict,
      rightWeight=weight, leftWeight=weight, aspect=20, fontsize=17
)
plt.tight_layout()
# plt.show() # to display
plt.savefig('metric-artefacts.pdf', bbox_inches='tight') # to save