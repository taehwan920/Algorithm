n = int(input())

words = []
for i in range(n):
    word = input()
    words.append(word)

last = words[0]
sample = list(last)
for i in range(1, n):
    for j in range(len(words[i])):
        if last[j] != words[i][j]:
            sample[j] = '?'
    last = words[i]

print(''.join(sample))
