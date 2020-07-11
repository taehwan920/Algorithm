n, k = map(int, input().split())
basic = set(list('anta') + list('tica'))
k -= len(basic)
words = []

for i in range(n):
    temp = input()

    if len(temp) > 8:
        temp = ''.join(
            sorted(list(filter(lambda x: x not in basic, list(temp[4:-4])))))
    else:
        temp = ''
    words.append(temp)

words = list(filter(lambda x: len(x) <= k, words))

if k == 0:
    print(words.count(''))
elif k < 0:
    print(0)
elif k > 0:
    # longest = max(words, key=lambda x : len(x))
    # longs = list(filter(lambda x : len(x) == len(longest), words))
    candidates = []
    for term in words:
        cnt = 0
        for i in range(len(words)):
            if words[i] in term:
                cnt += 1
        candidates.append(cnt)

    print(max(candidates))
