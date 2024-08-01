import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

numPapers = [68, 33, 22, 15, 12, 8, 4, 6]
problems = ['Test data generation', 'Test case prioritisation', 'Test case selection', 
          'Test suite evaluation', 'Test suite reduction', 'Fault localisation', 'New metric', 'Other']

colors = ['lavender', 'mediumturquoise', 'khaki', 'lightgreen', 'aqua', 'gold', 'orange']

# assign data
data = pd.DataFrame({'Problems': problems,
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
graph = plt.bar(data.Problems, data.NumPapers)#, color=colors)
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
             y+height*1.01 + 1.4,
             str(data.Percentage[i])+'%',
             ha='center',
             weight='bold')
    i += 1

plt.savefig("problems-histogram.jpg")
plt.show()