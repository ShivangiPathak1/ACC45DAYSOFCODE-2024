# cook your dish here
T=int(input())
for i in range(T):
    N,X=input().split()
    x=int(X)
    n=int(N)
    a=int(n/6)
    if n%6!=0:
        a=a+1 
    else:
        a=a 
    print(a*x)