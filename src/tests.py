import pi
from digits_test import count_digits
import khi2

digits = pi.get_digits()
l = len(digits)
count = count_digits(digits)
expected = {}
for i in range(0, 10) :
  expected[i] = l/10

from pprint import pprint

observed = count.values()
pprint(observed)
expected = expected.values()
pprint(expected)

for o, e in zip(observed, expected) :
  print(o, e)

r = khi2.test(observed, expected)
pprint(r)
