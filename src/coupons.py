import random
import pi
import pi_random
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
            if (i in rep):
                rep[i]+=1
            else :
                rep[len(rep)-1]+=1
            elements=list(all_digits)
            i=0
    return rep


def expected_coupons(obs,d=10):

    rep = {}
    totr=0
    t = len(obs)
    for e in obs.values():#we compute the total of different sequence
        totr+=e

    for r in range(t-1):#have all the differents r sequence
        if (r<d):
            rep[r]=0
        else :
            rep[r]=stirling(r-1,d-1)*(math.factorial(d)/(d**r))*totr

    rep[t]= 1 - (stirling(t-1,d)*(math.factorial(d)/(d**(t-1))))
    rep[t]*=totr
    return rep

def gen_python(size=1000000):# because there is one million decimal in pi file
    """ This function generate size discrete values by the python generator (between 0 and 1)
    and return all the values in a list  """

    digits=[]
    for i in range(size):
        digits.append(math.floor(random.random()*10))
    return digits

def gen_ours(size=1000000):
    """ This function generate size discrete values by our generator based on Pi
    and return all the values in a list  """

    digits=[]
    for i in range(size):
        digits.append(math.floor(pi_random.random()*10))
    return digits

def do_test(name, digits ,limit=85):#good value to have a good test
    """ This function is used to make the cupon collector test on the digits with a limited values"""

    print ("################################################")
    print (name)
    print ("################################################")

    observed = count(digits,limit)
    expected = expected_coupons(observed)

    test.make_test(observed, expected, 'Test du CDC : '+name, 'r', 'Nombre d\'occurences')



if __name__ == "__main__" :

    do_test("Les décimales de Pi",pi.get_digits())
    do_test("Le générateur de python",gen_python())
    do_test("Notre générateur",gen_ours())
