gaps={}

def mark(digits,a,b):
    rep = []
    for e in digits :
        value = float(e)/10
        if a<=value and value<=b:
            rep.append(True)
            #print (value,True)
        else :
            rep.append(False)
            #print (value,False)
    return rep

def realGaps(digits,r,a,b):

    marked = mark(digits,a,b)
    rep = {}

    for i in range(r+1):#initialise the list
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
    #on teste les gaps qui vont jusque 35

def expected_gaps(digits,r,a,b):
    rep={}
    p=(b-a)+0.1
    n=len(digits)
    for i in range(r+1):
        rep[i]= p*((1-p)**i)
        rep[i]*=n*p
    return rep

if __name__ == "__main__" :
  import pi
  digits = pi.get_digits()

  """test = realGaps([1,7,8,9,7,8],6,0,0.5)
  for e in test.items():
      print( e[0]," -- ",e[1])"""

  observed = realGaps(digits,25,0,0.5)
  expected = expected_gaps(digits,25,0,0.5)
  import test
  test.make_test(observed, expected, 'Gap', 'Tailles de gap', 'Nombre d\'occurences')
