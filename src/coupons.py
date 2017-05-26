import random
import pi
import math
import test
import scipy

def stirling(k, r) :
    """number of manner to make r groups with k choices - not recursive version"""
    return (1/math.factorial(r))*sum((-1)**(r-i)*scipy.special.binom(r, i)*i**k for i in range(r+1))

def count(digits,r,d=10):
    """count the numbers of digits met before having met all the differents digits """

    all_digits=[]
    for i in range(d):#init the list of possible digits
        all_digits.append(i)

    elements = list(all_digits)
    i = 0
    p=0#pointer in the string
    rep = {}

    for e in range(r+1) :#init the rep with 0
      rep[e] = 0

    while (p < len(digits)):

        if (len(elements)!=0):
            dig = int(digits[p])
            if dig in elements:
                elements.remove(dig)
            i+=1
            p+=1
        else :
            #print (i)
            if (i in rep):
                rep[i]+=1
            elements=list(all_digits)
            i=0
    return rep


def expected_coupons(obs,d=10):

    rep = {}
    totr=0
    for e in obs.values():#we compute the total of different sequence
        totr+=e

    for r in range(len(obs)):#have all the differents r sequence
        if (r<d):
            rep[r]=0
        else :
            rep[r]=stirling(r-1,d-1)*(math.factorial(d)/(d**r))*totr
    return rep

if __name__ == "__main__" :

    print ("################################################")
    print ("Test sur décimales de Pi")
    print ("################################################")
    digits = pi.get_digits()#str of digits
    observed = count(digits,101)#good value to have a good test
    expected = expected_coupons(observed)

    test.make_test(observed, expected, 'Collectionneur de coupons', 'r', 'Nombre d\'occurences')

    print ("################################################")
    print ("Test sur python")
    print ("################################################")

    digits =[]
    for i in range(1000000):# because there is one million decimal in pi file
        digits.append(math.floor(random.random()*10))

    observed = count(digits,101)#good value to have a good test
    expected = expected_coupons(observed)

    test.make_test(observed, expected, 'Collectionneur de coupons', 'r', 'Nombre d\'occurences')
