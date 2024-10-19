# cook your dish here
T=int(input())
for i in range(T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    if x<y:
        print("BIKE")
    elif x==y:
        print("SAME")
    elif x>y:
        print("CAR")