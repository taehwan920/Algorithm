n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        if trees[i] > mid:
            # 설정된 중간값보다 큰 나무만 잘리므로 이 조건을 붙여서
            cnt += trees[i] - mid
            # 자른 나무의 길이를 더해준다.
    if m <= cnt:
        # 이 경우만이 요구치보다 같거나 클때 -> 즉 문제의 조건을 만족하는 조건이므로 이렇게 설정.
        start = mid + 1
        result = mid
        # 문제의 요구를 만족하는것 중 가장 작은 값이 저장되게 되므로 start값을 재설정하는 파트에만 새 mid값을 result에 저장하는 코드가 등장하게 됨.
    else:
        end = mid - 1
print(result)
