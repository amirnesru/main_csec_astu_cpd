n=int(input())
arr=list(map(int,input().split()))
a=0
b=0
for i in range(n):
    if arr[i]!=-1:
        a+=arr[i]
    else:
        if a==0:
            b+=1
        else :
            a-=1       
print(b)             
