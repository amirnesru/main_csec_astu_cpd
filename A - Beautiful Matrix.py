for i in range(5):
        x= list (map(int,input().split()))
        if 1 in x:
                a=i
                b=x.index(1)
print(abs(a-2)+abs(b-2))       
