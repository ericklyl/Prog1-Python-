from f1 import f_mdc

def main():
    count= 1
    while (count <= 4):
        count += 1
        a = int(input())
        b = int(input())
        c = int(input())
        f1 = f_mdc(a,b,c)
        print(f'MDC=({a},{b},{c}) = {f1}')

if __name__=="__main__":
  main()