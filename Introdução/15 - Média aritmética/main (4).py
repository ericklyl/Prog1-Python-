#Faça um programa que receba 4 (quatro) notas de um aluno (0 a 100) e apresente a sua média aritmética final.

def main():
  n1 = float(input('Digite um valor: '))
  n2 = float(input('Digite um valor: '))
  n3 = float(input('Digite um valor: '))
  n4 = float(input('Digite um valor: '))
  soma = (n1 + n2+ n3+ n4)  
  media = soma/4
  
  print(media)
    
if __name__ =="__main__":
    main()