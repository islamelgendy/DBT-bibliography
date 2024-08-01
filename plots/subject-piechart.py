import time
import plotly.express as px
import plotly.graph_objects as go

data = [113, 12, 10, 18, 4, 3, 3, 3, 1]
labels = ['Stand-alone', 'Model-based', 'Web', 
          'NNs Models', 'GUI', 'Autonomous Vehicles', 'Compilers', 'Mobile', 'Database']

colors = ['lavender', 'mediumturquoise', 'khaki', 'lightgreen', 'lightyellow', 'gold', 'linen']
# colors = ["0.1", "0.25", "0.4", "0.55", "0.7", "0.85", "0.95"]

fig = go.Figure(data=[go.Pie(labels=labels, values=data, textinfo='label+percent', textfont_size=17, marker_colors=colors,
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

fig.write_image("subjects-dist.pdf", format="pdf")
fig.show()