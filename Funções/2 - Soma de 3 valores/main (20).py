def f_soma(x,y,z):
    soma = x + y + z
    return soma
def main():
    a = int(input("digite um valor: "))
    b = int(input("digite um valor: "))
    c = int(input("digite um valor: "))

    soma = f_soma(a,b,c)
    print(soma)
    
    
    
    
if __name__=="__main__":
    main()