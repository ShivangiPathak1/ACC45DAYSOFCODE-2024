# cook your dish here
T=int(input())
for i in range(T):
    P,Q,R,S=input().split()
    p=int(P)
    q=int(Q)
    r=int(R)
    s=int(S)
    if p>q+r+s or r>p+q+s or q>p+r+s or s>p+q+r:
        print('Yes')
    else:
        print('No')