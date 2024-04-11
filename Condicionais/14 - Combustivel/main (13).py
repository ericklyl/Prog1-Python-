def main():
    Al = float(input())
    T = input()
    if T == "A":
        preço  = 2.90 * Al
        if Al <= 20:
            preço = preço - (preço * (3/100))
        else:
            preço = preço - (preço * (5/100))
    elif T == "G":
        preço = 3.30 * Al
        if Al <= 20:
            preço = (preço - (preço * 4/100))
        else:
            preço = (preço - (preço * 6/100))
    print(f'{preço:.2f}')
    
if __name__ == "__main__":
    main()