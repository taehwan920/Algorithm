class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        c = capacity
        nums = [0 for i in range(1001)]

        for i in range(len(trips)):
            num, s, e = trips[i]
            for j in range(s, e):
                nums[j] += num
                if nums[j] > capacity:
                    return False
        return True

# 시간복잡도를 n^2에서 n으로 바꾸는 방법


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        c = capacity
        nums = [0 for i in range(1001)]

        for trip in trips:
            num, s, e = trip
            nums[s] += num
            nums[e] -= num

        caps = 0
        for item in nums:
            caps += item
            if caps > c:
                return False
        return True
