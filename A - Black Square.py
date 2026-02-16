arr=list(map(int,input().split()))
s=input()
a=0
for i in range( len(s)):
    b=int(s[i])
    a+=arr[b-1]
print(a)
