# cook your dish here
T=int(input())
for i in range(T):
    X,Y,R=input().split()
    x=int(X)
    y=int(Y)
    r=int(R)
    x=x+r//30 
    if x%y==0:
        print(x//y)
    else:
        print((x//y)+1)