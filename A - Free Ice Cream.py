n,x=map(int, input().split())
count=0
for i in range(n):
    a=input()
    y = int(a.replace(" ", ""))
   
    if y>0 or x+y >=0:
        x+=y
    else :
        count+=1       
print(x,count)
