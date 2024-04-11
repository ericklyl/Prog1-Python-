def main():
    branco = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    frase = input("").upper()
  
    for c in range(len(frase)):
        if (frase[c] == " "):
            branco += 1
        elif (frase[c] == "A"):
            a += 1
        elif (frase[c] == "E"):
            e += 1
        elif (frase[c] == "I"):
            i += 1    
        elif (frase[c] == "O"):
            o += 1    
        elif (frase[c] == "U"):
            u += 1
            
    print(f'ESPAÇOS EM BRANCO = {branco}')
    print(f'A = {a}')
    print(f'E = {e}')
    print(f'I = {i}')
    print(f'O = {o}')
    print(f'U = {u}')           

if __name__ == "__main__":
  main()