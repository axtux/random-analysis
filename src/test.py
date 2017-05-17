from pprint import pprint
import khi2
import plotme
from _is_ import is_float

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

def make_test(observed, expected, name='', x_name='', y_name='') :
  x = list(observed.keys())
  
  y = {}
  y['Valeur observée'] = list(observed.values())
  y['Valeur attendue'] = list(expected.values())
  
  disp = dict(y)
  disp['A'+name] = x
  display(disp, name)
  
  
  k = khi2.test(y['Valeur observée'], y['Valeur attendue'])
  result = {}
  result['$\\alpha$'] = []
  result['AValeur'] = []
  result['Limite'] = []
  result['Résultat'] = []
  
  for alpha in sorted(k.keys()) :
    result['$\\alpha$'].append(alpha)
    result['AValeur'].append(k[alpha][0])
    result['Limite'].append(k[alpha][1])
    result['Résultat'].append('réussi' if k[alpha][2] else 'échoué')
  
  display(result, '$\\chi^2$')
  
  plotme.linechart((x, y), name, x_name, y_name)
  plotme.barchart((x, y), name, x_name, y_name)


def display(dic, name='') :
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
      data = dic[k][i]
      if is_float(data) :
        data = round(data, 3)
      row.append(str(data))
    
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
  
  print(latex_format(name, head, table))

def latex_format(name, head, table) :
  # tabular
  s = '\\begin{figure}[h]\n'
  s += '\\centering\n'
  s += '\\begin{tabular}{|'
  for h in head :
    s += 'r|'
  s += '}\n'
  
  s += '\\hline\n'
  for h in head :
    s += h + ' & '
  s = s[:-3]+'\\\\\n'
  s += '\\hline\n'
  for row in table :
    for data in row :
      s += data + ' & '
    s = s[:-3]+'\\\\\n'
  s += '\\hline\n'
  
  s += '\\end{tabular}\n'
  s += '\\caption{Tableau de '+name+'}\n'
  s += '\\end{figure}\n'
  
  s+= '\n'
  
  # image
  s += '\\begin{figure}[h]\n'
  s += '\\centering\n'
  image_name = '../chart_images/'+plotme.filename(name)+'_bar_chart.png'
  s += '\\includegraphics[scale=0.25]{'+image_name+'}\n'
  s += '\\caption{Graphique de '+name+'}\n'
  s += '\\end{figure}\n'
  
  return s

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
