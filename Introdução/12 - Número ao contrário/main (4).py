#Faça um programa que receba um número inteiro de 3 dígitos e apresente esse número ao contrário. Ex: 123 >> 321  ;  981 >> 189

def main():
  n1 = int(input())
  c = n1 // 100
  d = (n1%100)//10
  u = n1 % 10
  inv = (u * 100) + (d * 10) + (c)
  print(inv)
if __name__ == "__main__":
  main()