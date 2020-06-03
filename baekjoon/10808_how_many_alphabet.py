s = input()
alpha = [0 for i in range(26)]
for i in s:
    alpha[ord(i)-ord('a')] += 1
for i in alpha:
    print(i, end=" ")
