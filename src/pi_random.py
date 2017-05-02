import pi
import time

digits = pi.get_digits()
if digits == None :
  exit('Need digits from pi module')

l = len(digits)
path = 15

# duplicate some digits to get path digits at the end
digits = digits + digits[:path]

# add randomness to start point with ms time
i = int(time.time()*1000) % l

def random() :
  global i
  # IDEA get path from pi digits ?
  i = (i+path)%l
  
  s = digits[i:i+path]
  
  return int(s)* 10**(-path)


if __name__ == "__main__" :
  for k in range(0, 5) :
    print(random())
