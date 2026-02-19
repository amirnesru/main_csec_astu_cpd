k,l,m,n,d=[int(input()) for _ in range(5)]
a=True
b=0
while d!=0:
    for i in [k,l,m,n]:
        if d % i ==0:
             b+=1
             break
    d-=1         
print(b)        
