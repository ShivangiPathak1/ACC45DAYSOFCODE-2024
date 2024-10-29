# cook your dish here
T=int(input())
for i in range(T):
    a=int(input())
    if a==1:
        print('NO')
    else:
       p=True
       for i in range(2,a):
           if a%i==0:
              p=False
              break
       if p==True:
           print('Yes')
       else:
           print('No')