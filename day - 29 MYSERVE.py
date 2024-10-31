# cook your dish here
T=int(input())
for i in range(T):
    P,Q=input().split()
    p=int(P)
    q=int(Q)
    x=p+q 
    if x%4==0 or x%4==1:
        print("Alice")
    else:
        print("Bob")