import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.patches

ax = plt.gca()
ax.axis("equal")

data = [53, 29, 20, 11, 10, 8, 7]# 2, 2, 1, 1, 1]# 7]
prob = ['TDG', 'TCP', 'TCS', 'TSE', 'TSR', 'FL', 'Other'] # 'New Metric', 'Test Reuse', 'Test Adapt.', 'BVA', 'Teach DBT']
probfull = ['Test data generation', 'Test case prioritisation', 'Test case selection', 'Test suite evaluation', 'Test suite reduction', 'Fault localisation', 'Other'] # 'New Metric', 'Test Reuse', 'Test Adapt.', 'BVA', 'Teach DBT']
# plt.xticks(range(len(data)), labels)
# plt.xlabel('Software Testing Problem')
# plt.ylabel('Number of Studies')
#plt.title('I am title')
pie, texts = plt.pie(data)

# Adding legend
#plt.legend(pie, probfull, loc="upper left")

plt.legend(pie,probfull, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, bbox_transform=plt.gcf().transFigure)
#plt.bar(range(len(data)), data) 
plt.tight_layout()
plt.show()