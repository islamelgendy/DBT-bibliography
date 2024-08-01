import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

numPapers = [35, 31, 21,
        12, 9, 9, 
        9, 9, 6, 
        5, 4, 
        3, 3,  
        3, 13]
artefacts = ['Input', 'Test script', 'Feature',
          'Hybrid', 'Execution', 'Transition', 
          'Output', 'Coverage',  'GUI', 
          'Semantic', 'Trigger',
          'Path', 'Context', 
          'Test steps', 'Other']

colors = ['lavender', 'mediumturquoise', 'khaki', 'lightgreen', 'aqua', 'gold', 'orange']

# assign data
data = pd.DataFrame({'Aretefact': artefacts,
                     'NumPapers': numPapers
                     })
 
# display data
print(data)

total_papers = data.NumPapers.sum()
print('Total number of papers: %s' % total_papers)

# compute percentage of each format
percentage = []
 
for i in range(data.shape[0]):
    pct = (data.NumPapers[i] / total_papers) * 100
    percentage.append(round(pct, 1))
 
# display percentage
print(percentage)
 
# display data
data['Percentage'] = percentage
print(data)

plt.figure(figsize=(8, 8))
plt.ylabel('Number of Studies')
# colors_list = ['Red', 'Orange', 'Blue', 'Purple']
graph = plt.bar(data.Aretefact, data.NumPapers, color=colors)
# plt.xticks(xLabels)
plt.xticks(rotation=45)
plt.tight_layout()
# plt.title('Percentage of runs scored by MS Dhoni across all formats')
 
i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
     
    plt.text(x+width/2,
             y+height*1.01,
             str(data.NumPapers[i]),
             ha='center',
             weight='bold')
    plt.text(x+width/2,
             y+height*1.01 + 0.7,
             str(data.Percentage[i])+'%',
             ha='center',
             weight='bold')
    i += 1

plt.savefig("artefacts-histogram.jpg")
plt.show()