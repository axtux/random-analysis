import random
import pi
import pi_random
import math
import test

def binomial(n, k) :
  return math.factorial(n) / math.factorial(k) / math.factorial(n-k)

def stirling(k, r) :
    """number of manner to make r groups with k choices, iterative version"""

    return sum((-1)**(r-i)*binomial(r, i)*i**k for i in range(r+1)) / math.factorial(r)

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
    totr=sum(i for i in obs.values())
    t = len(obs)
    
    for r in range(t-1):#have all the differents r sequence
        if (r<d):
            rep[r]=0
        else :
            rep[r]=stirling(r-1,d-1)*(math.factorial(d)/(d**r))*totr

    rep[t]= 1 - (stirling(t-1,d)*(math.factorial(d)/(d**(t-1))))
    rep[t]*=totr
    return rep

def generate_digits(generator, size) :
    """generate digits from random number generator in [0, 1[
    and return all the values in a list  """
    return [int(generator.random()*10) for i in range(size)]

def do_test(name, digits, limit=85):
    """ This function is used to make the cupon collector test on the digits with a limited values
    limit : 85 is a good value with 10^6 digits to avoid empty classes"""
    line = '##' + '#'*len(name) + '##'
    print (line)
    print ('# ' + name + ' #')
    print (line)

    observed = count(digits,limit)
    expected = expected_coupons(observed)

    test.make_test(observed, expected, 'Test du CDC : '+name, 'r', 'Nombre d\'occurences')



if __name__ == "__main__" :
  pi_digits = pi.get_digits()
  size = len(pi_digits)
  
  do_test("Les décimales de Pi", pi_digits)
  do_test("Le générateur de python", generate_digits(random, size))
  do_test("Notre générateur", generate_digits(pi_random, size))
