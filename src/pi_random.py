import pi
import time

digits = pi.get_digits()
if digits == None :
  exit('Need digits from pi module')

l = len(digits)

# number of digits to use to make random number
path = 15

# when i is l-1, you should still get path digits
digits = digits + digits[:path]

# add randomness to start point with ms time
i = int(time.time()*1000) % l

def random() :
  global i
  
  i = (i+path)%l
  
  s = digits[i:i+path]
  
  return int(s)* 10**(-path)


if __name__ == "__main__" :
  for k in range(0, 5) :
    print(random())
