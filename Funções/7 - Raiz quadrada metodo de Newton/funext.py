def f_quadp(n1):
  v = (n1//2)+1
  for l in range(1,v+1):
    if (n1 > l**2):
      d = n1 - l**2
    else:
      d = l**2-n1
    if (l == 1):
      difer = d
      q = l
    elif (d < difer):
      difer = d
      q = l
  return q

def f_quad(n1):
  quadperf =  f_quadp(n1)
  quad = (n1+(quadperf**2))/(2*quadperf)
  return quad
  