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

    for i in range(r+1):#initialise les gaps à 0
        rep[i]=0

    inGap = False
    gap = 0
    for i in range(len(marked)):
        if (not marked[i]):
            gap +=1
            inGap=True
        if (marked[i]):
            rep[gap]+=1
            gap=0
            inGap=False
    return rep
      
def expected_gaps(obs,r,a,b):
    rep={}
    p=(b-a)
    totGap=0
    for n in obs.values() :#numbers of gap total (proche de nombres*p)
         totGap+=n
    #print (totGap)
    for i in range(r+1):
        rep[i]= p*((1-p)**i)
        rep[i]*=totGap
    return rep

if __name__ == "__main__" :

  import pi_random

  #initialisation, il est conseiller de prendre a ou b qui vaut 0 ou 1
  n = 1000000
  a = 0
  b = 1/2
  #test sur notre générateur
  generated = pi_random.generate(n)
  observed = gaps(generated,25,a,b)#on limite les gaps à 35 car dépasse pas en général, bonne valeur
  expected = expected_gaps(observed,25,a,b)
  import test
  test.make_test(observed, expected, 'Gap', 'Tailles de gap', 'Nombre d\'occurences')

  #test sur le générateur de python
