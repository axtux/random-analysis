from _is_ import *

def count_digits(digits) :
  # init count dictionary
  count = {}
  for i in range(0, 10) :
    count[i] = 0
  
  if is_int(digits) or is_float(digits) :
    digits = str(digits)
  
  try :
    iter(digits)
  except TypeError :
    return print('digits is not iterable')
  
  for d in digits :
    try :
      int_d = int(d)
    except ValueError :
      continue
    count[int_d] = count[int_d] + 1
  
  return count
  
if __name__ == "__main__" :
  import pi
  digits = pi.get_digits()
  count = count_digits(digits)
  from pprint import pprint
  pprint(count)
