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
