def main():
  
  s = 0
  sneg = 0
  cont = 0
  media = 0
  
  for c in range(0,5):
    n = int(input(''))
    if (n > 0):
      s += n 
    else:
      sneg += n
      cont += 1
  media = sneg/cont
  print(s, media)
  
if __name__ == "__main__":
  main()