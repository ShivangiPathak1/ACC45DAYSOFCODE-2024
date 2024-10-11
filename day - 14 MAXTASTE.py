# cook your dish here
T=int(input())
for i in range(T):
    a,b,c,d=input().split()
    A=int(a)
    B=int(b)
    C=int(c)
    D=int(d)
    if A>B:
        x=A 
    else:
        x=B 
    if C>D:
        y=C 
    else:
        y=D 
    print(x+y)