#Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.


def main(): 
    n1 = int(input('Qual o numero? '))
    if (n1%2) == 0:
        print('Par')
    else:
        print('Impar')
if __name__ =='__main__':
    main()