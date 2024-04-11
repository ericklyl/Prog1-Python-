def main():

    n1 = int(input('qual o primeiro valor? '))
    n2 = int(input('qual o segundo valor? '))
    n3 = int(input('qual o terceiro valor? '))
    if n1>n2>n3:
        print( n1)
    if n2>n1>n3:
        print(n2)
    if n2>n3>n1:
        print(n2)
    if n1> n3> n2:
        print(n1)
    if n3 > n2 > n1:
        print(n3)
    else:
        print(n3)
    
if __name__ == "__main__":
    main()