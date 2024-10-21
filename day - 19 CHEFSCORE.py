# cook your dish here
T=int(input())
for i in range(T):
    N,X,Y=input().split()
    n=int(N)
    x=int(X)
    y=int(Y)
    if y%x==0:
        print("Yes")
    else:
        print("No")