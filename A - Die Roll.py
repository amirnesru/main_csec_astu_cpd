
Y, W = map(int, input().split())
a = max(Y, W)
b = 7 - a
if b % 6 == 0:
    print(f"1/1")
elif b % 3 == 0:
    print(f"{b//3}/2")
elif b % 2 == 0:
    print(f"{b//2}/3")
else:
    print(f"{b}/6")
