def main():
    d = input("Data de nascimento: ")
    di = int(d[0:2])
    m = int(d[3:5])
    a = int(d[6:])
    if (m == 1):
      mes = "janeiro"
    elif (m == 2):
      mes = "fevereiro"
    elif(m == 3):
      mes = "março"
    elif(m == 4):
      mes = "abril"
    elif(m == 5):
      mes = "maio"
    elif(m == 6):
      mes = "junho"
    elif(m == 7):
      mes = "julho"
    elif(m == 8):
      mes = "agosto"
    elif(m == 9):
      mes = "setembro"
    elif(m == 10):
      mes = "outubro"
    elif(m == 11):
      mes = "novembro"
    elif(m == 12):
      mes = "dezembro"

    print(di,"de", mes,"de", a) 
if __name__ == "__main__":
    main()