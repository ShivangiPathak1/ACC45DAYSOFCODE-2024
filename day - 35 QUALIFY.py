# cook your dish here
T=int(input())
for i in range(T):
    X,A,B=input().split()
    x=int(X)
    a=int(A)
    b=int(B)
    if (a+b*2)>=x:
        print("Qualify")
    else:
        print("NotQualify")