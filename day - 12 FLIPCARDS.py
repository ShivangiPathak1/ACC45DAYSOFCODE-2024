# cook your dish here
T=int(input())
for i in range(T):
    N,X=input().split()
    n=int(N)
    x=int(X)
    y=int(n-x)
    if x>=y:
        print(y)
    else:
        print(x)
    