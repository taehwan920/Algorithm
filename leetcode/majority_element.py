class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sample = list(set(nums))

        return max(sample, key=lambda x: nums.count(x))
