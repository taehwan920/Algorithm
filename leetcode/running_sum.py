class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        result = []
        for num in nums:
            temp += num
            result.append(temp)

        return result
