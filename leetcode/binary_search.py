class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if mid < 0 or mid >= len(nums):
                break
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid

        return -1

# 배열 인덱스 찾는 이진 탐색 문제의 경우 배열 길이를 벗어나는 경우의 탈출조건을 반드시 걸어둘 것..
