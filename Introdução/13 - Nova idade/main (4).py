def main():

    dias = int(input('Quantos dias de idade tem? '))
    
    data = dias // 365
    porc = dias % 365
    meses = porc // 30
    d = porc % 30
    
    print((data), (meses), (d))

if __name__ == "__main__":
    main()