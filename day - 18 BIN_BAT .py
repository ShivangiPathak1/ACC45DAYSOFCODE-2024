# cook your dish here
T=int(input())
for i in range(T):
    N,A,B=input().split()
    n=int(N)
    a=int(A)
    b=int(B)
    t=2
    c=0
    while (t<n+1):
        t=t*2
        c=c+1
        
    print(c*a+(c-1)*b)
   