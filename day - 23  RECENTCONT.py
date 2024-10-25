# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    X=input().split()
    l=0
    s=0
    for j in X:
        if j=='LTIME108':
            l+=1 
        elif j=='START38':
            s+=1
    print(s,l)