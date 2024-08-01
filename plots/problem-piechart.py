import time
import plotly.express as px
import plotly.graph_objects as go

data = [68, 33, 22, 15, 12, 8, 4, 6]
labels = ['Test data generation', 'Test case prioritisation', 'Test case selection', 
          'Test suite evaluation', 'Test suite reduction', 'Fault localisation', 'New metric', 'Other']
# labelsper = ['Test data generation \n 37.9%', 'Test case prioritisation \n 22.1%', 'Test case selection \n 14.5%', 
#           'Test suite evaluation \n 7.6%', 'Test suite reduction \n 6.9%', 'Fault localisation \n 6.2%', 'Other \n 4.8']

colors = ['lavender', 'mediumturquoise', 'khaki', 'lightgreen', 'aqua', 'gold', 'orange']
# colors = ["0.1", "0.25", "0.4", "0.55", "0.7", "0.85", "0.95"]

fig = go.Figure(data=[go.Pie(labels=labels, values=data, textinfo='label+percent', textfont_size=20, marker_colors=colors,
                             insidetextorientation='radial')])


# fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=13,
#                   marker=dict(colors=colors, line=dict(color='#000000', width=2)))

# df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
# fig = px.pie(df, values='pop', names='country',
#              title='Population of American continent',
#              hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})
# fig.update_traces(textposition='inside', textinfo='percent+label')

#Actual plot
fig.update_layout(autosize=False,
    width=900,
    height=700,
    showlegend=False)

fig.update_layout(legend=dict(y=0.8))

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
)
fig.write_image("pie.pdf", format="pdf")

time.sleep(2)

fig.write_image("problems-dist.pdf", format="pdf")
fig.show()