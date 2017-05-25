from scipy.stats import chi2
table = [0.1,0.05,0.01,0.001]

def test(observed, expected) :
  ol = len(observed)
  el = len(expected)
  if not ol == el :
    return print('observed length {} must match expected length {}'.format(ol, el))

  df = ol - 1
  if df < 1 :
    return print('degree of freedom {} must be at least 1'.format(df))

  x = 0
  corr = -0.5 if df == 1 else 0

  for o, e in zip(observed, expected) :
    if e == 0 :
      print('skipping values {}, {} because expected is 0'.format(o, e))
      continue
    x = x + (o - e + corr)**2/e

  x = round(x, 3)

  results = {}
  for alpha in table :
    limit = chi2.ppf(1-alpha,df)
    results[alpha] = (x, limit, x < limit)

  return results
