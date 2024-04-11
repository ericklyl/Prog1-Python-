from funext import f_quad

def main():
  n1 = int(input())
  while (n1 >= 0):
    q = f_quad(n1)
    print(f'N={n1:.4f} RAIZ={q:.6f}')
    n1 = int(input())
  return 0


if __name__=="__main__":
  main()