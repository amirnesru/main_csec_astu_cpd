n=int (input())
arr=list(map(int,input().split()))
a=0
b=0
turn=0
while len (arr)!=0:
    if turn==0:
        a+=max(arr[0],arr[-1])
        arr.remove(max(arr[0],arr[-1]))
        turn=1
    else:
        b+=max(arr[0],arr[-1])
        arr.remove(max(arr[0],arr[-1]))
        turn=0


print(a,b)
