# cook your dish here
T=int(input())
for i in range(T):
    N,A,B=input().split()
    n=int(N)
    a=int(A)
    b=int(B)
    c=0
    d=0
    for j in range(1,n+1):
        if j%2==0:
            c=c+1
        else:
            d=d+1
    print((c*a)+(d*b))
