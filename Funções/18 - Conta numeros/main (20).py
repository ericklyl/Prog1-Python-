def f_conta(n,id):
  count = 0
  q = 0
  
  while(id >= count):
    n = str(n)
    count = str(count)
    for x in range(len(count)):
      if(n == count[x]):
        q += 1
    n = int(n)
    count = int(count)
    count += 1
  return q

def main():
  n = int(input())
  id = int(input())
  print(f_conta(n,id))
    
  return 0

if __name__ == "__main__":
  main()