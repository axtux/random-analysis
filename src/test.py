import pprint
import khi2
import plotme

"""
Get expected uniform classes from observed classes
"""
def expected_uniform(observed) :
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
  from pprint import pprint
  
  x = list(observed.keys())
  
  y = {}
  y['observed'] = list(observed.values())
  y['expected'] = list(expected.values())
  
  k = khi2.test(y['observed'], y['expected'])
  pprint(k)
  
  if plot :
    plotme.linechart((x, y), name)
    plotme.barchart((x, y), name)
