import time
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Survey/sankey.csv') #Read above CSV

#Sort by Source and then Destination
df['source'] = pd.Categorical(df['source'], ['Formal','Informal', 'Unemployed', 'Inactive'])
df['destination'] = pd.Categorical(df['destination'], ['Formal','Informal', 'Unemployed', 'Inactive', 'SelfEmployed'])
df.sort_values(['source', 'destination'], inplace = True)
df.reset_index(drop=True)

mynode = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ['Formal', 'Informal', 'Unemployed', 'Inactive', 'Formal', 'Informal', 'Unemployed', 'Inactive', 'SelfEmployed'],
      x = [0.001, 0.001, 0.001, 0.001, 0.999, 0.999, 0.999, 0.999, 0.999],
      y = [0.001, 75/285, 160/285, 190/285, 0.001, 75/285, 130/285, 215/285, 255/285], 
    #   x = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    #   y = [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
      color = ["#305CA3", "#C1DAF1", "#C9304E", "#F7DC70", "#305CA3", 
               "#305CA3", "#C1DAF1", "#C9304E", "#F7DC70", "#305CA3",
               "#305CA3", "#C1DAF1", "#C9304E", "#F7DC70", "#305CA3",
               "#305CA3", "#C1DAF1", "#C9304E", "#F7DC70", "#305CA3"])

mylink = dict(
    source = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3], 
    target = [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
    value = df.value.to_list())

fig = go.Figure(data=[go.Sankey(
    arrangement='snap',
    node = mynode,
    link = mylink
)])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=20)

time.sleep(2)
fig.write_image("Sankey.pdf", format="pdf")
fig.show()