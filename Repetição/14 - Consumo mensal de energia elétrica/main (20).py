def main():
  #preço = float(input('Qual o preço? '))
  #nmrcons = int(input('Qual o numero do consumidor? '))
  #qntdmes = int(input('Qual a quantidade consumida em um mes? '))
 #cod = input('Qual o codigo? ').upper
  maior = 0
  menor = 0
  count = 0
  total = 0
  media = 0
  somageral = 0
  somaR = 0
  somaC = 0
  somaI = 0
  

  preço = float(input())
  cod = int(input())
  while(cod != 0):
    qntdmes = int(input())
    tipo = input().upper()
    count += 1
    mult = preço * qntdmes
    if count == 1:
      maior = qntdmes
      menor = qntdmes
    else:
      if(qntdmes > maior):
        maior = qntdmes
      if(qntdmes < menor):
        menor = qntdmes
    if(tipo == 'R'):
      somaR += qntdmes
    if(tipo == 'C'):
      somaC += qntdmes
    if (tipo == 'I'):
      somaI += qntdmes
    print(cod, mult)
    cod = int(input())

  somageral += (somaR + somaC + somaI)
  media = somageral/count
  print(maior)
  print(menor)
  print(somaR)
  print(somaC)
  print(somaI)
  print(media)
if __name__=="__main__":
  main()