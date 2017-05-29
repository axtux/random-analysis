import pi_random
import random
import test

gaps={}

def in_gap(n, a, b) :
  """test if n is bigger or equal than a and lower or equal than b"""
  return a <= n and n <= b

def gaps(numbers, limit, a, b) :
  rep = {}
  for i in range(limit+1):#initialize the gaps to 0
    rep[i]=0
  
  gap = 0
  for n in numbers :
    # marked number in gap
    if in_gap(n, a, b) :
      # store bigger gaps in last item
      if gap > limit :
        gap = limit
      rep[gap] += 1
      gap = 0
    else :
      gap +=1
  
  return rep

def expected_gaps(obs, limit, a, b) :
  rep={}
  p=(b-a)
  totGap=0
  for n in obs.values() : #numbers of total gap (near numbers*p)
    totGap+=n
  
  print('totGap={}'.format(totGap))
  
  for i in range(limit) :
    rep[i] = p * (1-p)**i * totGap
  # for n > i, (1-p)^(i+1)
  rep[limit]= (1-p)**(i+1) * totGap
  
  return rep

def compare_test(n, a, b, limit) :
  """generate n numbers from both pi and python generators, make gap test and compare generators"""
  
  print ("#######################################")
  print ("# Test du gap sur le générateur de Pi #")
  print ("#######################################")
  generated = pi_random.generate(n)
  observed = gaps(generated, limit, a, b)
  expected = expected_gaps(observed, limit, a, b)
  
  test.make_test(observed, expected, 'Pi Gap', 'Tailles de gap', 'Nombre d\'occurences')
  
  
  print ("###########################################")
  print ("# Test du gap sur le générateur de Python #")
  print ("###########################################")
  generated=[random.random() for i in range(n)]
  observed = gaps(generated, limit, a, b)
  expected = expected_gaps(observed, limit, a, b)
  
  test.make_test(observed, expected, 'Python Gap', 'Tailles de gap', 'Nombre d\'occurences')

if __name__ == "__main__" :
  # run test with 1.000.000 numbers, between 0 and 1/2, limit 15
  compare_test(10**6, 0, 1/2., 15)
  
