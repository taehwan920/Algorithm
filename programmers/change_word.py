import heapq


def compare(str1, str2):
    difference = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            difference += 1
            if difference > 1:
                return False
    return True


def solution(begin, target, words):
    n = len(words)
    q = []
    heapq.heappush(q, [0, 0, begin])
    while q:
        cnt, idx, now = heapq.heappop(q)
        if now == target:
            return cnt
        if idx >= n:
            continue
        if compare(now, words[idx]):
            heapq.heappush(q, [cnt + 1, idx + 1, words[idx]])
            heapq.heappush(q, [cnt, idx + 1, now])
        else:
            heapq.heappush(q, [cnt, idx + 1, now])
    return 0

# 처음 작성한 코드. 배열 순서대로만 탐색해서 그런지 테스트케이스 1개가 실패가 떴음.


def compare1(str1, str2):
    difference = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            difference += 1
            if difference > 1:
                return False
    return True


def solution1(begin, target, words):
    q = []
    visited = [False for i in range(len(words))]
    heapq.heappush(q, [0, begin])
    while q:
        cnt, now = heapq.heappop(q)
        if now == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                if compare(now, words[i]):
                    visited[i] = True
                    heapq.heappush(q, [cnt + 1, words[i]])
    return 0

# 다시 작성한 코드. 현재의 단어랑 한글자만 차이나는단어 + 아직 간 적 없는 단어에 한해서 q에 넣어 bfs를 돌렸다.


def solution(begin, target, words):
    memory = {}

    for word in words:
        for i, c in enumerate(word):
            key = word[:i] + '$' + word[i+1:]
            if not memory.get(key):
                memory[key] = []
            memory[key].append(word)

    parents = {begin: None}
    frontier = [begin]
    step = 0

    while frontier:
        _next = []
        for word in frontier:
            neighbors = []
            for i, e in enumerate(word):
                key = word[:i] + '$' + word[i+1:]
                if key in memory:
                    neighbors += memory[key]

            for neighbor in neighbors:
                if neighbor == target:
                    return step + 1

                if neighbor not in parents:
                    parents[neighbor] = word
                    _next.append(neighbor)

        frontier = _next
        step += 1

    return 0
# dict 자료형을 적극적으로 활용한 풀이방법. 소요 시간도 굉장히 짧다.
# 각 단어들을 $을 활용해 한글자씩 비운 걸 dict로 모아서 저장하는 요령을 숙지해두자
