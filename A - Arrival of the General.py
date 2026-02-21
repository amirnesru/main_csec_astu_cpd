n=int(input())
arr=list(map(int , input().split()))
a=arr.index(max(arr))
arr.reverse()
b=arr.index(min(arr))
b= (n-1)-b
if a>b:
    print(a+(n-2)-b)
else:
    print(a+(n-1)-b)    
