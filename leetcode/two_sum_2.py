class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            temp_sum = numbers[l] + numbers[r]
            if temp_sum == target:
                return [l+1, r+1]
            elif temp_sum < target:
                l += 1
            else:
                r -= 1
