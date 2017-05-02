table = {
  '0.1' : {
     1 :  2.706,
     2 :  4.605,
     3 :  6.251,
     4 :  7.779,
     5 :  9.236,
     6 : 10.645,
     7 : 12.017,
     8 : 13.362,
     9 : 14.684,
    10 : 15.987,
    11 : 17.275,
    12 : 18.549,
    13 : 19.812,
    14 : 21.064,
  },
  '0.05' : {
     1 :  3.841,
     2 :  5.991,
     3 :  7.815,
     4 :  9.488,
     5 : 11.070,
     6 : 12.592,
     7 : 14.067,
     8 : 15.507,
     9 : 16.919,
    10 : 18.307,
    11 : 19.675,
    12 : 21.026,
    13 : 22.362,
    14 : 23.685,
  },
  '0.01' : {
     1 :  6.635,
     2 :  9.210,
     3 : 11.345,
     4 : 13.277,
     5 : 15.086,
     6 : 16.812,
     7 : 18.475,
     8 : 20.090,
     9 : 21.666,
    10 : 23.209,
    11 : 24.725,
    12 : 26.217,
    13 : 27.688,
    14 : 29.141,
  },
  '0.001' : {
     1 : 10.828,
     2 : 13.816,
     3 : 16.266,
     4 : 18.467,
     5 : 20.515,
     6 : 22.458,
     7 : 24.322,
     8 : 26.125,
     9 : 27.877,
    10 : 29.588,
    11 : 31.264,
    12 : 32.910,
    13 : 34.528,
    14 : 36.123,
  },
}

def khi2(alpha, df) :
  alpha = str(alpha)
  if not alpha in table :
    return print('alpha {} not in table'.format(alpha))
  df = int(df)
  if not df in table[alpha] :
    return print('df {} not in table'.format(df))
  return table[alpha][df]

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
  print('df is {}, corr is {}'.format(df, corr))
  for o, e in zip(observed, expected) :
    x = x + (o - e + corr)**2/e
  
  results = {}
  for alpha in table.keys() :
    limit = khi2(alpha, df)
    results[alpha] = (x, limit, x < limit)
  
  return results
