# cook your dish here
T=int(input())
for i in range(T):
    A,B=input().split()
    a=int(A)
    b=int(B)
    c=21-(a+b) 
    if c<=10:
        print(c)
    else:
        print("-1")
