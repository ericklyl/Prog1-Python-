def main():
  
    n1 = int(input('qual o primeiro valor? '))
    n2 = int(input('qual o segundo valor? '))
    n3 = int(input('qual o terceiro valor? '))
    if n1>n2>n3:
        print(n3, n2, n1)
    if n2>n1>n3:
        print(n3, n1, n2)
    if n2>n3>n1:
        print(n1, n3, n2)
    if n1> n3> n2:
        print(n2, n3, n1)
    if n3 > n2 > n1:
        print(n1, n2, n3)
    else:
        print(n2, n1, n3)
    
if __name__ == "__main__":
    main()