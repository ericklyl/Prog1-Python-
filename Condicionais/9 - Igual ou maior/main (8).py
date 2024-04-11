def main():

    n1 = int(input('Qual o valor? '))
    n2 = int(input('Qual o valor? '))
    n3 = int(input('Qual o valor? '))
    if n1 > n2 > n3:
        print(n1 + n2)
    if n1 > n3 > n2:
        print(n1 + n3)
    if n2 > n1> n3:
        print(n2 + n1)
    if n2 > n3 > n1:
        print(n2 + n3)
    if n3 > n1 > n2:
        print(n3 + n1)
    if n3 > n2 > n1:
        print(n3 + n2)
    
if __name__ == '__main__':
    main()