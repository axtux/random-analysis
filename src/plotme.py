import plotly
from plotly.graph_objs import Bar, Figure, Scatter, Layout
from plotly.figure_factory import create_distplot

"""
  Plot an array like
  { x : [y1, y2, y3], ...
  { 1 : [val1, val2, val3],
    2 : [val1, val2, val3],
    ...
  }
"""
def plot(data, file_name='image', chart_name='Chart', x_name='X Axis', y_name='Y Axis', trace_names=[]) :
  (x, y) = data
  data = []
  # create data object from traces
  for name in y :
    data.append(Scatter(x=x, y=y[name], mode='lines+markers', name=name))
  
  # name axes
  layout = Layout(
      title=chart_name,
      xaxis=dict(title=x_name),
      yaxis=dict(title=y_name)
  )
  # plot to file
  fig = Figure(data=data, layout=layout)
  plotly.offline.plot(fig, filename=file_name+'.html', image='png', image_filename=file_name, image_height=1200, image_width=1600)

"""
plot barchart from
(
  [x1, x2, x3],
  {
    'data1' : [y1, y2, y3],
    'data2' : [y1, y2, y3],
  }
)
"""
def histo(data, file_name='image', chart_name='Chart', x_name='X Axis', y_name='Y Axis') :
  (x, y) = data
  data = []
  # create data object from traces
  for name in y :
    data.append(Bar(x=x, y=y[name], name=name))
  
  # name axes
  layout = Layout(
      title=chart_name,
      xaxis=dict(title=x_name),
      yaxis=dict(title=y_name),
      barmode='group'
  )
  
  # plot to file
  fig = Figure(data=data, layout=layout)
  plotly.offline.plot(fig, filename=file_name+'.html', image='png', image_filename=file_name, image_height=1200, image_width=1600)

"""
  From :
  {
    x1 : [y1, y2, y3],
    x2 : [y1, y2, y3],
    ...
  }
  To :
  (
    [x1, x2, ...],
    {
      'data1' : [y1, y1, ...],
      'data2' : [y2, y2, ...],
      'data3' : [y3, y3, ...],
    }
  )
"""
def split_data(data, names) :
  x = list(data.keys())
  
  # create y list for each value
  y = {}
  for name in names :
    y[name] = []
  
  # fill with data
  for k in x :
    for i in range(0, len(names)) :
      y[names[i]].append(data[k][i])
  
  return (x, y)
