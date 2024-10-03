# cook your dish here
T=int(input())
for i in range(T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    #X and Y are the time required to solve problems A and B in minutes respectively.
    
    a=500-x*2
    b=1000-(x+y)*4
    s=a+b 
    A=500-y*4
    B=1000-(x+y)*2
    S=A+B 
    if s>S: 
        print(s)
    else:
        print(S)
    
    
    