import pi
from digits_test import count_digits
from test import expected_uniform, make_test


"""
Digists test
"""
digits = pi.get_digits()
observed = count_digits(digits)
expected = expected_uniform(observed)
make_test(observed, expected)

