import pi
import time
from _is_ import is_int

DEFAULT_PATH = 17

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
  set_path(DEFAULT_PATH)

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

def generate(number) :
  return [random() for i in range(number)]

def period() :
  i = 1
  while (i*l)%path != 0 :
    i += 1
  return i*l/path

init()
if __name__ == "__main__" :
  num = generate(20)
  for i in num :
      print (i)
