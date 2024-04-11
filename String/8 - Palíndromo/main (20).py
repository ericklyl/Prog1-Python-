def main():
    frase = input().upper()
    frase2 = ""
    
    for i in range(len(frase)):
        if (frase[i] != " "):
            frase2 += frase[i].upper()
        
    if (frase2 == frase[::-1]):
        print('É PALÍNDROMO')
    else: 
        print("NÃO É PALÍNDROMO")
    
    
    
    
if __name__=="__main__":
    main()