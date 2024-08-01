import plotly.graph_objects as go

# data
label = ["Euclidean", "Jaccard", "Edit", "Hamming", "Manhattan", "OtherG", "Specialised", 
         "Input", "TestScript", "Hybrid", "Execution", "Transitions", "Coverage", "Feature", "Output", "GUI", "Other"]
source = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
          1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
          5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
          6, 6, 6, 6, 6, 6, 6, 6, 6, 6] # 7 source nodes
target = [7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13, 
          7, 8, 9, 10, 11, 12, 13] # 10 target nodes

value = [3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7, 
         3, 8, 2, 6, 8, 6, 7]

# colors for links in Sankey
color_link = [
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold',
    'beige', 'blue', 'darkcyan', 'lightgray', 'lightsalmon', 'greenyellow', 'coral', 'lightgreen', 'crimson', 'gold'
    #'#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5', '#f71b1b', '#1b7ef7', '#12e23f', '#f78c1b', '#9BD937', '#7FC241'
]


# data to dict, dict to sankey
link = dict(source = source, target = target, value = value, color = color_link)
node = dict(label = label, pad = 20, thickness = 10)
data = go.Sankey(link = link, node = node)

# graph the Sankey
fig = go.Figure(data)
fig.update_layout(
    hovermode = 'x',
    title = 'Customer Migration from Campaing Pre to Post',
    font = dict(size=10, color='black'),
    paper_bgcolor = '#ffffff'
)

fig.show()