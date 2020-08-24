words = []

for i in range(int(input())):
  words.append(input())

words = list(set(words))

s_words = sorted(sorted(words, key=lambda x: x), key=lambda x : len(x))

for w in s_words:
  print(w)