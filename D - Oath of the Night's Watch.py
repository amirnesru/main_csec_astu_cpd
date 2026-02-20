n=int(input())
arr=list(map(int,input().split()))
a=arr.count(max(arr))
b=arr.count(min(arr))
if max(arr) == min(arr):
    print(0)
else:    
    print(len(arr)-(a+b))


