table = {
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

def khi2(alpha, ddl) :
  alpha = str(alpha)
  if not alpha in table :
    return print('alpha {} not in table'.format(alpha))
  ddl = int(ddl)
  if not ddl in table[alpha] :
    return print('ddl {} not in table'.format(ddl))
  return table[alpha][ddl]

def test(observed, expected) :
  ol = len(observed)
  el = len(expected)
  if not ol == el :
    return print('observed length {} must match expected length {}'.format(ol, el))
  
  ddl = ol - 1
  if ddl < 1 :
    return print('degree of freedom {} must be at least 1'.format(ddl))
  
  x = 0
  corr = -0.5 if ddl == 1 else 0
  for o, e in zip(observed, expected) :
    x = x + (o - e + corr)**2/e
  
  results = {}
  for alpha in table.keys() :
    limit = khi2(alpha, ddl)
    results[alpha] = (x, limit, x < limit)
  
  return results
