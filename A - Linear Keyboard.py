t=int(input())
for i in range(t):
    letters=input()
    s=input()
    a=0
    for j in range(len(s)-1):
        a+=abs(letters.index(s[j+1])-letters.index(s[j]))
    print(a)    
