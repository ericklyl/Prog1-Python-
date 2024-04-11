def main():
  #idade = int(input())
  media = 0
  soma = 0
  count = 0
  idade = int(input())
  while(idade > 0):
    #idade = int(input(''))
    soma += idade
    count += 1
    idade = int(input())
    media = soma/count
  print(media)
  
if __name__=="__main__":
  main()