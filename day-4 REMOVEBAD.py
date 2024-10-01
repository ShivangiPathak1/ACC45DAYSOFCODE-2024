T=int(input())
for i in range(T):
    N=int(input())
    S=map(int,input().split())
    L=list(S)
    dict={}
    for j in L:
        if j in dict:
            dict[j]+=1
        else:
            dict[j]=1
    Max=max(dict.values())
    print(N-Max)
        