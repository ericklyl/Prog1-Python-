#Faça um Algoritmo para ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO. UTILIZE O COMANDO WHILE.

def main():
    n1 = int(input())
    contador = 1
    while(contador <= n1):
        print(contador)
        contador += 1
    
    return 0
if __name__ == "__main__":
    main()