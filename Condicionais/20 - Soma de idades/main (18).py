def main():
    hn = int(input())
    hv = int(input())
    mv = int(input())
    mn = int(input())
    if (hn > hv) and (mv > mn): 
      s = hv + mn
      m = hn * mv
      print(s, m)
    elif (hn > hv) and (mn > mv):
      s = hn + mv
      m = hv * mn
      print(s, m)
    elif (hv > hn) and (mv > mn):
      s = hn + mv
      m = hn * mv
      print(s, m)
    else:
        s = hv + mv
        m = hn + mn
        print(s, m)
if __name__ == "__main__":
    main()