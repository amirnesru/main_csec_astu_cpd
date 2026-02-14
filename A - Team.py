n = int(input())
a=0
for i in range (n):
    arr=list(map(int , input().split()))
    x=arr.count(1)
    if x>=2:
        a+=1
print(a)        
