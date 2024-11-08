# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    a=input().split()
    count=0
    for j in a:
        if int(j)==1:
            count=count+1
        elif int(j)==-1:
            count=count-1
    if count%2==0:
        print(abs(count//2))
    elif N%2==1:
        print(-1)
    elif count==0:
        print(0)
        