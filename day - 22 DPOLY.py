# cook your dish here
T=int(input())
for  i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    count=0
    for j in range(N):
        if A[j]!=0:
            count=j
    print(count)