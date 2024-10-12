# cook your dish here
T=int(input())
for i in range(T):
    N,K,M=input().split()
    n=int(N)
    k=int(K)
    m=int(M)
    if n%(k*m)==0:
        print(int(n/(k*m)))
    else:
        print(int(n/(k*m))+1)
    