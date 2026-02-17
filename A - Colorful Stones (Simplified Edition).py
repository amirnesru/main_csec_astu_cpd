s=input()
t=input()
a=0
b=1
for i in range(len(t)):
     if s[a]==t[i]:
          b+=1
          a+=1
print(b)
