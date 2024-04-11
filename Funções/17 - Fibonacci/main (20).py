def f_fibo(n):
  ultimo=0
  penultimo=1
  
  if (n==1) or (n==2):
      print("1")
  else:
    count=1
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)

    
def main():
  n = int(input('Quantos termos serão somados? '))
  f = f_fibo(n)
  #print(f)


if __name__=="__main__":
  main()