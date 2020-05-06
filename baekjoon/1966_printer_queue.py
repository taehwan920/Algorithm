T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(doc, i) for i, doc in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


# 문제를 찬찬히 뜯어보면서 생각할것...
# 세번 풀었는데도 제대로 못풀었다.. ㅜㅜ
