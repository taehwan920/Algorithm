import heapq


def solution(operations):
    heap = []
    for order in operations:
        st, num = order.split()
        num = int(num)
        if st == 'I':
            heapq.heappush(heap, num)
        else:
            if heap:
                if num == 1:
                    heap.sort()
                    heap.pop()
                else:
                    heapq.heappop(heap)
    heap.sort()
    return [heap[-1], heap[0]] if heap else [0, 0]
