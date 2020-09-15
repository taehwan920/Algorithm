class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)

# 딴사람 풀이


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.count(0)
        for i in range(temp):
            nums.remove(0)
            nums.append(0)
        # 이렇게 하면 0의 갯수만큼만 돌면 돼서 훨씬 빠름?
