# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    if a>b and a>c and a>50:
        print('A')
    elif b>a and b>c and b>50:
        print('B')
    elif c>a and c>b and c>50:
        print('C')
    else:
        print('NOTA')