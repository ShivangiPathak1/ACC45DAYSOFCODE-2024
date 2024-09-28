# cook your dish here
T=int(input())
for I in range(T):
    N=int(input())
    S=input()
    c=0
    for j in S:
        if j in 'aeiou':
            c=0
        else: 
            c=c+1 
        if c>=4:
            print("no")
            break
    if c<4:
        print("yes")
        
        
        
    
        
        
    