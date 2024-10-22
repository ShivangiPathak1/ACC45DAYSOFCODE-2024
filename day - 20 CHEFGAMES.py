# cook your dish here
T=int(input())
for i in range(T):
    a,b,c,d=input().split()
    x=int(a)
    y=int(b)
    z=int(c)
    p=int(d)
    
    if x+y+z+p==0:
        print("In")
    else:
        print("Out")