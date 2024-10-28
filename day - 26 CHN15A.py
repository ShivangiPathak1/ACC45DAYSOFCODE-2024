# cook your dish here
T=int(input())
for i in range(T):
    N,K=input().split()
    n=input().split()
    c=0
    for j in range(int(N)):
        a=int(n[j])+int(K)
        if a%7==0:
            c+=1
    print(c)