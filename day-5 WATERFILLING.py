# cook your dish here
T=int(input())
for i in range(T):
    B=map(int,input().split())
    if sum(B)<2:
        print('Water filling time')
    else:
        print('Not now')