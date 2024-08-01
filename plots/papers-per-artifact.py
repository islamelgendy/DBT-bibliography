import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


data = [29, 26, 6, 2, 3, 9, 3, 5, 
        2, 8, 4, 2, 8, 2, 8, 3,
        1, 3, 3, 1, 1, 1, 11]
labels = ['Input', 'Test Script', 'Output', 'Requirements', 'Path', 'Execution', 'Context', 'GUI', 
          'Graph', 'Transitions', 'Triggers', 'Mutants', 'Feature', 'Behavioral', 'Coverage', 'Semantic',
          'Test Rep.', 'Test Steps', 'SPL conf.',  'Social', 'Function', 'Running time', 'Hybrid']

fig, ax = plt.subplots()
plt.xticks(range(len(data)), labels)
plt.xlabel('Diversity Artifact')
plt.ylabel('Number of Studies')
#plt.title('I am title')
plt.bar(range(len(data)), data) 
plt.xticks(rotation=45)
fig.tight_layout()
plt.show()