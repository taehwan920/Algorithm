from collections import Counter
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        check_num = []
        sample = list(set(barcodes))

        for s in sample:
            heapq.heappush(check_num, [-barcodes.count(s), s])

        result = []

        while len(check_num) >= 2:
            a_cnt, a = heapq.heappop(check_num)
            b_cnt, b = heapq.heappop(check_num)

            result.append(a)
            result.append(b)

            if a_cnt + 1:
                heapq.heappush(check_num, [a_cnt + 1, a])
            if b_cnt + 1:
                heapq.heappush(check_num, [b_cnt + 1, b])

        if check_num:
            result.append(check_num[0][1])
        return result

# 이건 그냥 개수 파악해서 했을때. 소요시간 9500ms 나옴


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        check_num = []
        counted = Counter(barcodes)

        for k, v in list(counted.items()):
            heapq.heappush(check_num, [-v, k])

        result = []

        while len(check_num) >= 2:
            a_cnt, a = heapq.heappop(check_num)
            b_cnt, b = heapq.heappop(check_num)

            result.append(a)
            result.append(b)

            if a_cnt + 1:
                heapq.heappush(check_num, [a_cnt + 1, a])
            if b_cnt + 1:
                heapq.heappush(check_num, [b_cnt + 1, b])

        if check_num:
            result.append(check_num[0][1])
        return result

# Counter 모듈 사용시. 소요시간 552ms로 9초나 줄어버림;
