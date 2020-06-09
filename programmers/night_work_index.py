import heapq


def solution(n, works):
    works = list(map(lambda x: -1 * x, works))
    heapq.heapify(works)

    for _ in range(n):
        temp = heapq.heappop(works)
        if temp >= 0:
            return 0
        temp += 1
        heapq.heappush(works, temp)

    result = 0
    for task in works:
        result += task ** 2
    return result

# 계속해서 정렬해줘야하는 풀이의 경우 heap을 이용하면 간단한데 계속 까먹어서 삽질을 자주 한다.. heap을 항상 염두에 둘 것
