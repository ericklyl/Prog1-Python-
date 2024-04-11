#Faça um programa que leia 2 strings e informe se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

def main():
    st1 = input()
    st2 = input()
    comprimento1 = len(st1)
    comprimento2 = len(st2)
    if (comprimento1 == comprimento2):
        print('MESMO TAMANHO')
    else:
        print('TAMANHO DIFERENTE')
        
    if (st1 == st2):
        print('CONTEÚDO IGUAL')
    else:
        print('CONTEÚDO DIFERENTE')

if __name__=="__main__":
    main()