# cook your dish here
T=int(input())
for  i in range(T):
    N=int(input())
    a=input().split()
    c=0
    for j in range(len(a)-1):
        x=abs(int(a[j])-int(a[j+1]))-1
        c=c+x
    print(c)
        