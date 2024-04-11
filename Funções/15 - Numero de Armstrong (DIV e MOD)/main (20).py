def f_arms(a):
  p = f_taman(a)
  s = 0
  while (a > 0):
    r = a % 10
    s += r ** p
    a = a // 10
  return s


def f_taman(a):
  c = 0
  while (a > 0):
    c += 1
    a = a // 10
  return c


def f_vArm(a):
  return a == f_arms(a)

def main():
  for a in range(1,1000000):
    if (f_vArm(a)):
      print(a)
  return 0

if __name__ == "__main__":
  main()