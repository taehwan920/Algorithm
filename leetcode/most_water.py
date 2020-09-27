class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        result = 0
        l, r = 0, n-1

        while l < r:
            left = height[l]
            right = height[r]
            water = min(left, right) * (r - l)
            result = water if water > result else result

            if left < right:
                l += 1
            else:
                r -= 1

        return result

# 투 포인터 알고리즘.
# 여기서는 둘 중 더 큰 걸 가리키는 포인터는 그대로 두고, 더 작은 쪽을 다른 걸로 변경하면서 포인터 간격을 좁히는 방식으로 풀이함.
