def main():
  n = 1
  while(n != 1000000): 
    soma = 0
    for i in str(n):
      soma += int(i)**(len(str(n)))
    if (soma == n):
      print(soma)
    n += 1
  return 0

if __name__ == "__main__":    
  main()