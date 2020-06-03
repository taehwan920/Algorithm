s = input()

for i in range(len(s)):
    if s[i] != s[len(s)-1-i]:
        print(0)
        break
else:
    print(1)
