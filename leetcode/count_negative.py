def bts(arr):
    start = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if mid < 0:
            return len(arr)
        if mid >= len(arr):
            return 0
        if arr[mid] < 0:
            end = mid - 1
        else:
            start = mid + 1

    return len(arr[start:])


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for line in grid:
            neg += bts(line)

        return neg

# 음수의 개수를 파악하는 문제이므로 혹시 mid가 0보다 작으면 전부 음수라는 소리가 되고 배열 길이보다 커지면 전부 양수라는 뜻이므로 이에 해당하는 조건식을 추가해줌.
