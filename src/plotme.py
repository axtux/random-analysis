import os
import plotly
from plotly.graph_objs import Bar, Figure, Scatter, Layout

DIR_CHARTS='../charts'

"""plot linechart from
(
  [x1, x2, x3],
  {
    'data1' : [y1, y2, y3],
    'data2' : [y1, y2, y3],
  }
)
"""
def linechart(data, name='', x_name='X Axis', y_name='Y Axis') :
  (x, y) = data
  data = []
  # create data object from traces
  for trace_name in y :
    data.append(Scatter(x=x, y=y[trace_name], mode='lines+markers', name=trace_name))
  name += ' Line Chart'
  
  # name axes
  layout = Layout(
      title=name,
      xaxis=dict(title=x_name),
      yaxis=dict(title=y_name)
  )
  
  # plot to file
  offline_plot(name, data, layout)

"""plot barchart from
(
  [x1, x2, x3],
  {
    'data1' : [y1, y2, y3],
    'data2' : [y1, y2, y3],
  }
)
"""
def barchart(data, name='', x_name='X Axis', y_name='Y Axis') :
  (x, y) = data
  data = []
  # create data object from traces
  for trace_name in y :
    data.append(Bar(x=x, y=y[trace_name], name=trace_name))
  name += ' Bar Chart'
  
  # name axes
  layout = Layout(
      title=name,
      xaxis=dict(title=x_name),
      yaxis=dict(title=y_name),
      barmode='group'
  )
  
  # plot to file
  offline_plot(name, data, layout)

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
def split_data(data, names):
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

def offline_plot(name, data, layout):
  file_name = filename(name)
  
  fig = Figure(data=data, layout=layout)
  
  plotly.offline.plot(fig, filename=file_name+'.html', auto_open=False, image='png', image_filename=file_name, image_height=1200, image_width=1600)

def filename(chart_name):
  """lowercase and replace space by underscore"""
  return DIR_CHARTS+'/'+str(chart_name).lower().replace(' ', '_')

def init() :
  try :
    os.makedirs(DIR_CHARTS)
  except OSError :
    pass

init()
