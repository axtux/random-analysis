gaps={}

def mark(numbers,a,b):
    rep = []
    for n in numbers :
        if a<=n and n<=b:
            rep.append(True)
            #print (n,True)
        else :
            rep.append(False)
            #print (n,False)
    return rep

def gaps(numbers,r,a,b):

    marked = mark(numbers,a,b)
    rep = {}

    for i in range(r+1):#initialize the gaps to 0
        rep[i]=0
    gap = 0
    for i in range(len(marked)):
        if (not marked[i]):
            gap +=1
        if (marked[i]):
            rep[gap]+=1
            gap=0
    return rep

def expected_gaps(obs,r,a,b):
    rep={}
    p=(b-a)
    totGap=0
    for n in obs.values() :#numbers of total gap (near numbers*p)
         totGap+=n
    #print (totGap)
    for i in range(r+1):
        rep[i]= p*((1-p)**i)
        rep[i]*=totGap
    return rep

if __name__ == "__main__" :

  import pi_random
  import random
  #initialization, you might take a or b equals to 0 or 1
  n = 1000000
  a = 0
  b = 1/2

  #test on our generator
  print ("################################################")
  print ("Test sur Pi")
  print ("################################################")
  generated = pi_random.generate(n)
  observed = gaps(generated,35,a,b)
  expected = expected_gaps(observed,35,a,b)
  import test
  test.make_test(observed, expected, 'Gap', 'Tailles de gap', 'Nombre d\'occurences')

  #test on the python generator
  print ("################################################")
  print ("Test sur Python")
  print ("################################################")

  generated=[]
  for i in range(n):#init the generated numbers by python
      generated.append(random.random())

  #gaps length limited to 35 bacause it's a good value, it's generaly not overpassed
  observed = gaps(generated,35,a,b)#we can change 35 to a higher value if we want
  expected = expected_gaps(observed,35,a,b)
  import test
  test.make_test(observed, expected, 'Gap', 'Tailles de gap', 'Nombre d\'occurences')
