import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        f, s = 0, 0
        while f < len(nums1) and s < len(nums2):
            F, S = nums1[f], nums2[s]
            if F < S:
                for i in range(s, len(nums2)):
                    heapq.heappush(result, [F + nums2[i], [F, nums2[i]]])
                f += 1
            else:
                for i in range(f, len(nums1)):
                    heapq.heappush(result, [S + nums1[i], [nums1[i], S]])
                s += 1

        answer = []
        for i in range(k):
            if result:
                item = heapq.heappop(result)
                answer.append(item[1])
            else:
                break

        return answer
