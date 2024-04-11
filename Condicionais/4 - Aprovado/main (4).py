#Faça um programa que leia dois números inteiros, a e b. Se a for maior que b, apresente a soma dos dois, caso a seja menor ou igual a b, apresente o resultado da multiplicação dos dois. 


def main():
    n1 = int(input('A: '))
    n2 = int(input('B: '))
    if (n1 > n2):
        print(n1+n2)
    else:
        print(n1*n2)
if __name__=='__main__':
    main()