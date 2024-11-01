# cook your dish here
T=int(input())
for i in range(T):
    A,B=input().split()
    C,D=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    d=int(D)
    if a<=c and b<=d:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")