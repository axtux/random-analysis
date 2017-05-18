import random
import pi_random
import plotme
from _is_ import is_int, is_float
import math
import test

alphas = [0.001, 0.01, 0.05, 0.1]

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

def sample(generator, limit) :
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

def make_test(n=10**3) :
  name = 'Kolmogorov-Smirnov'
  (x, y_pi) = sample(pi_random, n)
  (x, y_py) = sample(random, n)
  
  pi_dn = max_gap((x, y_pi))
  py_dn = max_gap((x, y_py))
  
  y = {
    'Valeurs attendues' : y_pi['expected'],
    'Valeurs de Pi' : y_pi['observed'],
    'Valeurs de Python' : y_py['observed'],
  }
  data = (x, y)
  plotme.barchart(data, name)
  y['AX'] = x
  test.display(y, name, 6)
  
  result = {}
  result['$\\alpha$'] = []
  result['AValeur Pi'] = []
  result['AValeur Python'] = []
  result['Limite'] = []
  result['Meilleur'] = []
  
  for alpha in sorted(alphas) :
    result['$\\alpha$'].append(alpha)
    result['AValeur Pi'].append(pi_dn)
    result['AValeur Python'].append(py_dn)
    result['Limite'].append(dn(alpha, n))
    result['Meilleur'].append('Pi' if pi_dn < py_dn else 'Python')
  
  test.display(result, name, 6)
  

def dn(alpha, n) :
  if not is_int(n) :
    return print('n must be an integer')
  if n < 50 :
    return print('please use table for n < 50')
  if not is_float(alpha) :
    return print('alpha must be a float')
  if alpha <= 0 or alpha >= 1 :
    return print('alpha must be in ]0, 1[')
  
  return math.sqrt(-0.5*math.log(alpha/2))/math.sqrt(n)

if __name__ == '__main__' :
  make_test(10**5)
