n=int(input())
s=0
arr=[]
for i in range(n):
    exist,enter=map(int,input().split())
    s=s-exist+enter
    arr.append(s)
print(max(arr))    
