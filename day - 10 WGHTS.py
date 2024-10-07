# cook your dish here
T=int(input())

for i in range(T):
    W,X,Y,Z=input().split()
    w=int(W)
    y=int(Y)
    x=int(X)
    z=int(Z)
    if x+y+z==w or x+y==w or y+z==w or z+x==w or x==w or y==w or z==w:
        print('Yes')
    else:
        print('No')
        