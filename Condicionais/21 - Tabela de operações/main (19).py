def main():
    C = float(input())
    if (7 > C > 0):
    
        n1 = float(input())
        n2 = float(input())
       
        if (C == 1):
            res = n1 + n2
            print(res)
        elif (C == 2):
            res = n1 - n2
            print(res)
        elif (C == 3):
            res = n1 * n2
            print(res)
        elif (C == 4):
            res = n1 / n2
            print(res)
        elif (C == 5):
            res = n1 ** n2
            print(res)
        elif (C == 6):
            res = n1 ** (1/n2)
            print(res)
       
    else:
        print("OPERACAO INVALIDA")
        
if __name__ == "__main__":
    main()