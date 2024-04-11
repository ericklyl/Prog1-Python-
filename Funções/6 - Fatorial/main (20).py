def f_factorial(f1=1):
  f = 1
  for c in range(f1,0,-1):
    f *= c
  return f



def main():
    f1 = int(input())

    while f1 >= 0:
        #f1 = int(input())
        fac = f_factorial(f1)
        #while f1 >= 0:
        print(f'Fatorial({f1})={fac}')
        f1 = int(input())




if __name__=="__main__":
  main()