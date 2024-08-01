import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

numPapers = [35, 31, 30, 
        18, 18, 15, 
        13, 6, 6, 
        55, 41]
metrics = ['Euclidean distance', 'Edit distance', 'Jaccard distance',
          'Hamming distance', 'Manhattan distance', 'Normalised compression distance', 
          'Cosine distance', 'Identical Transition', 'Test set diameter', 
          'Other generic metrics', 'Other specialised metrics']
xLabels = ['Euclidean', 'Levenshtein', 'Jaccard',
          'Hamming', 'Manhattan', 'NCD', 
          'Cosine', 'Identical Transition', 'TSDm', 
          'Other generic', 'Other specialised']

colors = ['lavender', 'mediumturquoise', 'khaki', 'lightgreen', 'aqua', 'gold', 'orange', 'khaki', 'crimson', 'lightgrey', 'lightcoral']
# colors = ["0.1", "0.25", "0.4", "0.55", "0.7", "0.85", "0.95"]

# assign data
data = pd.DataFrame({'Metric': xLabels,
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
graph = plt.bar(data.Metric, data.NumPapers)#, color=colors)
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
             y+height*1.01 + 1.2,
             str(data.Percentage[i])+'%',
             ha='center',
             weight='bold')
    i += 1

plt.savefig("metrics-histogram.jpg")
plt.show()