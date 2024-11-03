# cook your dish here
N=int(input())
sp1=0
sp2=0
m=0
l=0
a=0

for i in range(N):
    P1,P2=map(int, input().split())
    sp1+=P1
    sp2+=P2
    a=abs(sp1-sp2)
    if a>m:
        m=a
        if sp1>sp2:
            l=1
        else:
            l=2

print(l,m)