class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

# 다른 풀이


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
        # 타겟 넘버에서 배열 내 숫자를 뺀 값이 dict안에 들어있으면 1. 더 앞에 있는 인덱스에서 2. 서로 더하면 타겟 넘버가 되는 숫자가 있음. 이 두가지가 증명이 되는 거라서 O(n)으로 충분히 풀 수 있었음.
