def main():
    n1 = int(input('Numero de eleitores: '))
    n2 = int(input('Numero de votos brancos: '))
    n3 = int(input('Numero de votos nulos: '))
    n4 = int(input('Numero de votos validos: '))
    br = (n2 * 100)/n1
    nu = (n3 * 100)/n1
    va = (n4 * 100)/n1
    print('BRANCOS= ',br,'%')
    print('NULOS= ',nu,'%')
    print('VALIDOS= ',va,'%')

if __name__ == '__main__':
    main()
