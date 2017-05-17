import random
import pi_random
import plotme

def uniform(x) :
  """uniform cumulative distribution function"""
  if x < 0 :
    return 0
  if x > 1 :
    return 1
  return x

def empirical(x, numbers) :
  """empirical distribution function"""
  acc = 0
  for n in numbers :
    if n <= x :
      acc = acc + 1
  return acc/len(numbers)

def sample(generator, limit=10**6) :
  """generate limit numbers and compare their distribution to uniform"""
  numbers = []
  for i in range(limit) :
    numbers.append(generator.random())
  
  # generate distributions
  x = []
  y = {}
  y['observed'] = []
  y['expected'] = []
  
  # sample
  for i in range(100) :
    i = i/100
    x.append(i)
    e = empirical(i, numbers)
    u = uniform(i)
    y['observed'].append(e)
    y['expected'].append(u)
  
  return (x, y)

def max_gap(data) :
  (x, y) = data
  max = 0
  for (o, e) in zip(y['observed'], y['expected']) :
    gap = abs(o-e)
    if gap > max :
      max = gap
  return max

def test() :
  pi_data = sample(pi_random)
  py_data = sample(random)
  
  pi_dn = max_gap(pi_data)
  py_dn = max_gap(py_data)
  
  plotme.barchart(pi_data, 'Pi Kolmogorov-Smirnov')
  plotme.barchart(py_data, 'Python Kolmogorov-Smirnov')
  
  print('Pi Dn is {}'.format(pi_dn))
  print('Py Dn is {}'.format(py_dn))

if __name__ == '__main__' :
  test()
