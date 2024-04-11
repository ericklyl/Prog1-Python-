def main():
    qa = float(input())
    qmax = float(input())
    qmin = float(input())
    qmedia = (qmax + qmin)/2
    if (qa >= qmedia):
        print("NÃO EFETUAR COMPRA")
    else:
        print('EFETUAR COMPRA')
if __name__ == "__main__":
    main()