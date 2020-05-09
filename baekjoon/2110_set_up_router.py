N, C = map(int, input().split())

house = []

for i in range(N):
    house.append(int(input()))

house.sort()

start = house[1] - house[0]
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] - value[0] >= mid:
            count += 1
            value = house[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
