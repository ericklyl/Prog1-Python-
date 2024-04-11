def main():
    S = input()
    Al = float(input())
    if (S == "M"):
        PI = (72.7 * Al) - 58
    else:
        PI = (62.1 * Al) - 44.7
    print(PI)
    
if __name__ == "__main__":
    main()