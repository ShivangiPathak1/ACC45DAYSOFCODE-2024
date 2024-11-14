# cook your dish here
T=int(input())
for i in range(T):
    N,X,P=input().split()
    n=int(N)
    x=int(X)
    p=int(P)
    y=int(n-x)
    if (x*3)-y>=p:
        print("Pass")
    else:
        print("Fail")