import file

pi_file = '../data/pi_1.000.000.txt'

def get_digits() :
  pi = file.get_contents(pi_file)
  if pi == None :
    print('Error reading file '+pi_file)
    return None
  
  pi = pi.replace('\r', '').replace('\n', '')
  
  # remove "3."
  return pi[2:]

if __name__ == "__main__" :
  digits = get_digits()
  if digits == None :
    exit()
  
  print('Pi 10 first digits are', digits[:10])
  #l = len(digits)
  print('Pi 10 last digits are', digits[-10:])
