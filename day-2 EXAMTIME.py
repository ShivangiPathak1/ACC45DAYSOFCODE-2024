# cook your dish here
T=int(input())
for i in range(T):
    DSA,TOC,DM=input().split()
    dsa,toc,dm=input().split()
    x=int(DSA)
    y=int(TOC)
    z=int(DM)
    a=int(dsa)
    b=int(toc)
    c=int(dm)
    if a+b+c>x+y+z:
        print('SLOTH')
    elif a+b+c<x+y+z:
        print('DRAGON')
    elif a+b+c==x+y+z:
        if a>x:
            print('SLOTH')
        elif x>a:
            print('DRAGON')
        elif x==a:
            if y>b:
                print('DRAGON')
            elif y<b:
                print('SLOTH')
            elif a==x and b==y and c==z:
                print('TIE')
        
    