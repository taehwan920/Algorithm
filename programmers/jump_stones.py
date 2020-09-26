def judge(stones, k, mid):
    now = 0

    for stone in stones:
        if stone < mid:
            now += 1
        else:
            now = 0
        if now >= k:
            return False
    return True


def solution(stones, k):
    left = 1
    # 최소 1명은 건널 수 있으므로.
    right = max(stones) + 1
    # left가 1부터 시작하므로 첫 mid값을 제대로 구하기 위해서 최대값에 1 더해줌

    while left < right - 1:
        # 꼴랑 둘이 붙어있을 땐 더이상 비울 가운데 돌이 없기 때문에 1만큼 간격을 띄운게 최소 차이가 되어야함.
        mid = (left + right) // 2

        if judge(stones, k, mid):
            left = mid
        else:
            right = mid
    return left

# 이분탐색 3번유형과 가장 흡사.
