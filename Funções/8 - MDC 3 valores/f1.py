def f_mdc(a,b,c):
    mdc=0
    i=2
    while i<a:
        if (a%i==0 and b%i==0 and c%i==0):
            mdc=i
        i=i+1
    return mdc