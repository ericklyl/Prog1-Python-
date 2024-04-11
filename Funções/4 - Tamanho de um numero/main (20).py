def f_dig(x):
    count = 0
    while (x > 0):
        count = count + 1
        x = x//10

    return count

def main():
    n = int(input("Informe um numero: "))
    ler = f_dig(n)
    print(ler)
    
    
    
    
if __name__ == "__main__":
    main()