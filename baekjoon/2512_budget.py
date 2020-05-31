n = int(input())
region = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(region)
# 이분 탐색 문제의 핵심은 start, end, 그리고 start와 end를 재설정할 기준 선정이다. 사실 이게 전부임.
# 처음엔 budget을 end로 삼았으나 틀려서 각 지방 별 요청 예산 중 가장 큰 것을 end로 삼았더니 풀렸다.
result = 0
if budget >= sum(region):
    print(max(region))
else:
    while start <= end:
        mid = (start + end) // 2
        # print(f's = {start} e = {end} m = {mid}')
        total = 0
        for i in range(n):
            total += min(region[i], mid)
        if total <= budget:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    print(result)
