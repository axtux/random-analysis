import random
import pi_random
import plotme

# uniform cumulative distribution function
def uniform(x) :
  if x < 0 :
    return 0
  if x > 1 :
    return 1
  return x

# empirical distribution function
def empirical(x, numbers) :
  acc = 0
  for n in numbers :
    if n <= x :
      acc = acc + 1
  return acc/len(numbers)



# generate numbers
numbers = []
for i in range(10**6) :
  numbers.append(pi_random.random())

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
  

plotme.plot((x, y))
