import pi

digits = pi.get_digits()
if digits == None :
  exit('Need digits from pi module')

l = len(digits)

# duplicate numbers to always be able to get 15 digits
digits = digits + digits

path = 15
i = l-path

def random() :
  global i
  # IDEA get path from pi digits ?
  i = (i+path)%l
  
  s = digits[i:i+15]
  
  return int(s)*1e-15


if __name__ == "__main__" :
  for k in range(0, 5) :
    print(random())
