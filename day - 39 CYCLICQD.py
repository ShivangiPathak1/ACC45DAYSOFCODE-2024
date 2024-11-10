# cook your dish here
T=int(input())
for i in range(T):
    A,B,C,D=input().split()
    if (int(A)+int(C))==180 and int(B)+int(D)==180:
        print("Yes")
    else:
        print("No")