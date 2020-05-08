docu = input()
word = input()

index = 0
result = 0
l_w = len(word)

while len(docu) - index >= len(word):
    if docu[index:index + len(word)] == word:
        result += 1
        index += l_w
    else:
        index += 1

print(result)
