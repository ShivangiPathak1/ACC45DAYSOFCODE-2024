# cook your dish here
T=int(input())
for t in range(T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    if x<y and y%x==0:
        print(int(y/x-1))
    elif x<y and y%x!=0:
        print(int(y/x))
    else:
        print(0)
