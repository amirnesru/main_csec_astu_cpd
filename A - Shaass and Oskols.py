n=int(input())
arr=list(map(int,input().split()))
m=int(input())
for i in range (m):
    x,y=map(int,input().split())
    if x<=n-1:
        arr[x]+=(arr[x-1]-y)
    if x-2>=0:    
        arr[x-2]+=(y-1)
    arr[x-1]=0  
for x in arr:
    print(x)  
           

