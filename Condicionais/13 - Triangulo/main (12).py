def main():

    A = float(input("Qual o valor? "))
    B = float(input("Qual o valor? "))
    C = float(input("Qual o valor? "))
    if (A + B) < C:
        print("NÃO É TRIÂNGULO")
    elif (A + C) < B:
        print("NÃO É TRIÂNGULO")
    elif (C + B) < C:
        print("NÃO É TRIÂNGULO")   
    elif A == B == C :
        print('EQUILÁTERO')
    elif A == C != B:
        print('ISÓSCELES')
    elif A == B != C:
        print('ISÓSCELES')
    elif A != B == C:
        print('ISÓSCELES')
    elif A != B != C:
        print('ESCALENO')
    elif (A + B) < C:
        print("NÃO É TRIÂNGULO")
    elif (A + C) < B:
        print("NÃO É TRIÂNGULO")
    elif (C + B) < C:
        print("NÃO É TRIÂNGULO")        
if __name__ == "__main__":
    main()