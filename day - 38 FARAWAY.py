# cook your dish here
T=int(input())
for i in range(T):
    N,M=input().split()
    n=int(N)
    m=int(M)
    A=input().split()
    dist=0
    for j in A:
        dist=dist+max(m-int(j),int(j)-1)
    print(dist)
