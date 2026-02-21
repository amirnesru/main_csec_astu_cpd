t=int(input())
for i in range(t):      
    n,m=map(int , input().split())
    s1=input()
    a=0
    for i in range (m):
        a+=7-len(set(s1))  
        for c in set(s1):
            s1 = s1.replace(c, "", 1)
        
    print(a)  
