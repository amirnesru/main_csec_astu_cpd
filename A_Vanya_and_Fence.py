n,h=map(int,input().split())
arr=list(map(int,input().split()))
a=0
for i in range(n):
    if arr[i]>h:
        a+=2
    else:
        a+=1    
print(a)
