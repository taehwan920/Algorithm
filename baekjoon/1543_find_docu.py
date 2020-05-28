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

# 밑엔 한번 더 풀었던 것. for문의 경우 i가 자동으로 1씩 늘어나기때문에 찾고자하는 단어의 길이에서 1을 빼준값을 더해줘야 했었다. 이걸 안해줘서 계속 틀렸다는 메세지가 나옴.
# 이런류의 문제 풀땐 주의해야할 것.
source = input()
that = input()
cnt = 0
jump = 0

for i in range(len(source)):
    if len(source) - i < len(that):
        break
    if jump:
        jump -= 1
        continue
    if source[i:i + len(that)] == that:
        jump += len(that)-1
        cnt += 1

print(cnt)
