# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    if a>=b and c>=b:
        print(a+c)
    elif a>=c and b>=c:
        print(a+b)
    elif b>=a and c>=a:
        print(b+c)