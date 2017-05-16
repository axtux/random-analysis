

def count(digits, seq_len = 5) :
  """count the number of different digits in each seq_len-digits sequence"""
  count = {}
  for i in range(1, seq_len+1) :
    count[i] = 0
  
  limit = len(digits)-seq_len+1
  for i in range(0, limit, seq_len) :
    sub = digits[i:i+seq_len]
    diff = count_different(sub)
    count[diff] = count[diff] + 1
  
  return count

def count_different(sequence) :
  return len(set(sequence))


def stirling(k, r) :
  """number of manner to make r groups with k choices"""
  if k < 1 or r < 1 or r > k :
    return None
  
  if r == 1 or r == k :
    return 1
  
  return stirling(k-1, r-1) + r*stirling(k-1, r)


def probability(k, r, l) :
  """probability to get r different elements within l-length sequence with k choices"""
  p = stirling(l, r)
  for i in range(k-r+1, k+1) :
    p = p * i
  return p/k**l

def expected_probability(observed) :
  seq_len = len(observed)
  
  total = 0
  for k in observed :
    total = total + observed[k]
  
  expected = {}
  for k in observed :
    p = probability(10, k, seq_len)
    expected[k] = round(total*p)
  return expected

if __name__ == "__main__" :
  import pi
  digits = pi.get_digits()
  observed = count(digits)
  expected = expected_probability(observed)
  import test
  test.make_test(observed, expected, 'Poker')
