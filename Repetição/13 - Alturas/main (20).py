def main():
    #sexo = input('Qual o sexo [M/F]? ').upper()
    #a = float(input('Qual a altura? '))
    maior = 0
    menor = 5
    count = 1
    somafem = 0
    countfem = 0
    mediafem = 0
    countman = 0
    for c in range(5):
        sexo = input('Qual o sexo [M/F]? ').upper()
        a = float(input('Qual a altura? '))
        if (a < menor):
            menor = a
        else:
            if (a > maior):
                maior = a
        if (sexo == 'F'):
            somafem += a
            countfem += 1
            mediafem = somafem/countfem
        if (sexo == 'M'):
            countman += 1
    print(maior)
    print(menor)
    print(mediafem)
    print(countman)
    


if __name__=='__main__':
    main()