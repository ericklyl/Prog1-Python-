#Desenvolva um programa que receba, enquanto o usuário responder sim "s", dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo), 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.



def main():
  opera = 0
  want = input().upper()
  while (want == 'S'):
    #want = input().upper()
    conta = int(input())
    n1 = int(input())
    n2 = int(input())
    if (conta == 1):
      opera = n1 + n2
    elif (conta == 2):
      opera = n1 - n2
    elif (conta == 3):
      opera = n1 * n2
    elif (conta == 4):
      opera = n1 / n2
    elif (conta == 5):
      opera = n1 ** n2
    elif (conta == 6):
      opera = n1 ** 1/2
    want = input().upper()
  print(opera)
      
      





if __name__=="__main__":
  main()