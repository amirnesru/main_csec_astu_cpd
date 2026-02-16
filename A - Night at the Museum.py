s = input()
a = 0
current = 'a'

for i in range(len(s)):
    d = min(abs(ord(s[i]) - ord(current)), 26 - abs(ord(s[i]) - ord(current)))
    a += d
    current = s[i]

print(a)
