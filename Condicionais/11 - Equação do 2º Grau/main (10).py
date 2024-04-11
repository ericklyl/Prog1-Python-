def main():
  
  a = float(input('Qual o valor de a? '))
  b = float(input('Qual o valor de b? '))
  c = float(input('Qual o valor de c? '))
  delta = b**2 - (4 * a * c) 
  if (delta > 0):
    raiz1 = (-b + delta **(1/2)) / (2 * a) 
    raiz2 = (-b - delta **(1/2)) / (2 * a) 
    print('\s*',raiz1, raiz2,'\s*')
    
  elif (delta == 0):
    raiz3  = (-b + (delta ** 1/2)) / (2 * a)
    print(raiz3)
  else:
   print('Não possui raiz\s')
    
if __name__ == '__main__':
  main()