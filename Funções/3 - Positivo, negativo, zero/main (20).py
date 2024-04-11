def f_arg(x):
    if (x > 0):
        return "P"
    elif(x == 0):
        return 'Z'
    else:
        return 'N'
    
def main():
    v = int(input("Coloque um valor: "))
    var = f_arg(v)
    print(var)
    
    
    
    
    
if __name__=="__main__":
    main()
