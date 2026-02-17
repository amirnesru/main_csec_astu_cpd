k,r=map(int , input().split())
a=k
b=1
while a % 10 !=r or a % 10!=0:
        if a%10==r or a%10==0:
            break
        b+=1
        a+=k
       
print(b)        
