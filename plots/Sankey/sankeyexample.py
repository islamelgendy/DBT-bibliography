import plotly.graph_objects as go

# data
label = ["High", "Medium", "Low", "High", "Meduim", "Low", "Lapsed"]
source = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2] #3 source nodes
target = [3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6] #4 target nodes
value = [548, 571, 129, 76, 303, 1513, 1537, 564, 189, 722, 1684, 1531]

# colors for links in Sankey
color_link = [
    '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5', 
    '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5', 
    '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5'
]

# data to dict, dict to sankey
link = dict(source = source, target = target, value = value, color = color_link)
node = dict(label = label, pad = 35, thickness = 10)
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