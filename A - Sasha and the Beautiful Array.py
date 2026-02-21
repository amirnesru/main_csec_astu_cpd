t=int(input())
for i in range(t):
    n=int(input())
    a=0
    arr=list(map(int,input().split()))
    arr.sort()
    arr.reverse()
    for i in range(n-1):
        a+=arr[i]-arr[i+1]
    print(a)    
