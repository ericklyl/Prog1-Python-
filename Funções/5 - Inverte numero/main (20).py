def f_digitos(n):
    count = 0
    while (n > 1):
        n = n/10
        count = count + 1
        
    return count

def f_inv(x):
    valor = 0
    tam = f_digitos(x)
    p = tam -1
    while (x > 0):
        resto = x % 10
        valor += resto * 10 ** p
        p = p-1
        x = x//10
    
    return valor

def main():
    x = int(input('Qual o valor: '))
    inv = f_inv(x)
    print(inv)
    
    
    
    
if __name__=="__main__":
    main()