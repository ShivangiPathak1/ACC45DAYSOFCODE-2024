# cook your dish here
T=int(input())
for i in range(T):
    A,B,K=input().split()
    a=int(A)
    b=int(B)
    k=int(K)
    c=abs(b-a)
    if c%k==0:
        print(int(c/k))
    else:
        print(int(c/k)+1)