# -*- coding: utf-8 -*-

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

def realGaps(marked,r):
    rep = {}
    for i in range(r):#initialise the list
        rep[i]=0
    inGap = False
    gap = 0
    for i in range(len(marked)):
        if (not marked[i]):
            gap +=1
            inGap=True
        if (marked[i] and inGap):
            rep[gap]+=1
            gap=0
            inGap=False
    return rep

def expected_gaps(digits,r,a,b):
    rep={}
    p=abs(a-b)
    n=len(digits)
    for i in range(r+1):
        rep[i]= p*((1-p)**i)
        rep[i]*=n
    return rep

if __name__ == "__main__" :
  import pi
  digits = pi.get_digits()
  observed = realGaps(mark(digits,0,0.5),35)
  expected = expected_gaps(digits,35,0,0.5)
  import test
  test.make_test(observed, expected, 'Gap', 'Tailles de gap', 'Nombre d\'occurences')
