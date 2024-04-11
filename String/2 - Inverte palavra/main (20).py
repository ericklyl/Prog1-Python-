def main():
    n = input().upper()
    for i in range(len(n)-1, -1, -1):
        print(n[i], end='')
        
    
    
if __name__=="__main__":
    main()