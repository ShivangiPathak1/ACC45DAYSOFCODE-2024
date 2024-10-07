# cook your dish here
T=int(input())
for i in range(T):
    N,A=input().split()
    n=int(N)
    a=int(A)
    b=n-a
    if b>=a:
        print(a)
    else:
        print(b)
