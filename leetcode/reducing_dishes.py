from collections import deque


def sum_arr(arr):
    n = len(arr)
    temp = 0
    for i in range(n):
        temp += arr[i] * (i+1)
    return temp


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        last = 0
        temp = deque([])
        for i in range(n):
            temp.appendleft(satisfaction[i])
            temp_sum = sum_arr(temp)
            if temp_sum < last:
                return last
            else:
                last = temp_sum
        return last
