# cook your dish here
T=int(input())
for i in range(T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    if 100*y/x>=50:
        print('Yes')
    else:
        print('No')