# cook your dish here
T=int(input())
for i in range(T):
    N,X=input().split ()
    n=int(N)
    x=int(X)
    if x%2==1 or n%2==0:
        print ('YES')
    else:
        print('NO')