# cook your dish here
from math import *
T=int(input())
for i in range(T):
    L,K =input().split()
    l=int(L)
    k=int(K)
    a=int(l%k!=0)
    print(a)
    