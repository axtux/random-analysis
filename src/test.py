from pprint import pprint
import khi2
import plotme


def expected_uniform(observed) :
  """Get expected uniform classes from observed classes"""
  total = 0
  keys = observed.keys()
  for k in keys :
    total = total + observed[k]
  
  n_class = len(keys)
  expected = {}
  for k in keys :
    expected[k] = total/n_class
  
  return expected

def make_test(observed, expected, name='', plot=True) :
  x = list(observed.keys())
  
  y = {}
  y['observed'] = list(observed.values())
  y['expected'] = list(expected.values())
  
  disp = dict(y)
  disp['X'] = x
  display(disp)
  
  
  k = khi2.test(y['observed'], y['expected'])
  pprint(k)
  
  if plot :
    plotme.linechart((x, y), name)
    plotme.barchart((x, y), name)
  

def display(dic) :
  head = sorted(dic.keys())
  if len(head) < 1 :
    return
  
  # length of columns
  l = len(dic[head[0]])
  
  table = []
  for i in range(l) :
    # make row
    row = []
    for k in head :
      row.append(display_number(dic[k][i]))
    
    # save it
    table.append(row)
  
  # get max length for each column
  max = []
  for k in head :
    max.append(len(k))
  
  for row in table :
    for i in range(len(max)) :
      l = len(row[i])
      if l > max[i] :
        max[i] = l
  
  separator = line_format(None, max, '-', '+-', '-+-')
  headline = line_format(head, max)
  
  print(separator)
  print(headline)
  print(separator)
  
  for row in table :
    line = line_format(row, max)
    print(line)
  
  print(separator)

def display_number(n) :
  return str(round(n, 3))


def left_pad(string, size, character=' ') :
  to_pad = size - len(string)
  
  # nothing to pad
  if to_pad < 1 :
    return string
  
  return to_pad*character + string

def line_format(data, size, char_pad=' ', start='| ', sep=' | ') :
  line = start
  
  if data == None :
    data = []
    for i in size :
      data.append('')
  
  for d, s in zip(data, size) :
    line += left_pad(d, s, char_pad) + sep
  return line[:-1]
