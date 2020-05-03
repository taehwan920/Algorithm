import heapq


def solution(scoville, K):
    heap = []
    for sco in scoville:
        heapq.heappush(heap, sco)

    count = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, (heapq.heappop(
                heap) + (2 * heapq.heappop(heap))))
        except IndexError:
            return -1
        count += 1
    return count

# 최소 힙이 디폴트인 heapq 모듈을 사용할 것.
# try/except도 항상 염두에 둘것.
