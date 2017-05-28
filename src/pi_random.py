import pi
import time
from _is_ import is_int


def init():
  """DO :
  - get pi digits and calculate len
  - set default path
  - add randomness to start point with ms time
  """
  global digits, l, i

  # get pi digits and calculate len
  digits = pi.get_digits()
  if digits == None :
    exit('Need digits from pi module')
  l = len(digits)

  # set default path
  set_path(17)

  # add randomness to start point with ms time
  i = int(time.time()*1000) % l

def set_path(p):
  """number of digits to use to make random number"""
  global path, mult, digits

  if not is_int(p):
    return print('p must be an integer')
  if p > l:
    return print('p max value is {}'.format(l))

  path = p
  # multiplication to get float in [0,1[
  mult = 10**(-path)
  # be able to get p digits when i is l-1
  digits = digits[:l] + digits[:path]

def random() :
  global i

  i = (i+path)%l

  s = digits[i:i+path]

  return int(s) * mult

def generate(number):
    init()
    rep=[]
    for i in range(number):
        rep.append(random())
    return rep

init()
if __name__ == "__main__" :
  num = generate(20)
  for i in num :
      print (i)
