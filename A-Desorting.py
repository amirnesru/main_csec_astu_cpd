t=int(input())
for i in range (t):
    n=int(input())
    arr=list(map(int , input().split()))
    diff=[] 
    for i in range(n-1):
        a=arr[i+1]-arr[i]
        diff.append(a)
    minimum=min(diff)
    if minimum<0:
        print(0)
    else:
        print (minimum//2+1)
