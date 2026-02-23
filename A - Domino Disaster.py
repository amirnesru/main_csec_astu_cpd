t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    bob=""
    for i in s:
        if i=="D":
            bob+="U"
        elif i=="U":
            bob+="D"    
        else:
            bob+=i
    print(bob)
