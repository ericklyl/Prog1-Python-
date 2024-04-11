def main():
    somapositivo = 0
    somanegativo = 0
    contneg = 0
    r = input("Deseja informar dados: ")


    while (r.upper() == 'S'):
        n = int(input())
        if (n >= 0):
            somapositivo += n
        else:
            somanegativo += n
            contneg += 1
        r = input("Deseja informar dados: ")
    print(somapositivo, somanegativo)

if __name__=="__main__":
    main()