# cook your dish here
T=int(input())
for  i in range(T):
    H,X,Y=input().split()
    h=int(H)
    x=int(X)
    y=int(Y)
    if (h-y)%x==0:
        print((h-y)//x+1)
    else:
        print((h-y)//x+2)