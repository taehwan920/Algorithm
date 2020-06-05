import heapq
n, k = map(int, input().split())
jewel = []
bags = []
# heap을 사용하여 시간복잡도 및 편의성을 챙김.
# 이 문제는 각 가방의 용량 범위 내에서 가장 가치가 큰 보석을 넣는것으로 풀 수 있는 그리디 알고리즘.

for i in range(n):
    wei, val = map(int, input().split())
    heapq.heappush(jewel, (wei, val))
# 보석의 무게 오름차 순으로 만들기 위해 최소 힙 배열 생성
for i in range(k):
    heapq.heappush(bags, int(input()))
# 가방도 용량 오름차순으로 최소 힙 배열 생성
result = 0
capable_gem = []

for _ in range(k):
    capacity = heapq.heappop(bags)
    # 가장 용량 작은 가방 하나 꺼내기

    while jewel and capacity >= jewel[0][0]:
        # 남은 보석이 있으며 꺼낸 가방의 용량이 가장 무게가 작은 보석보다 커야함.
        weight, value = heapq.heappop(jewel)
        heapq.heappush(capable_gem, -value)
        # 보석의 가치를 내림차순으로 정렬하기 위해 음수를 붙여 최대 힙을 만들어 줌.

    if capable_gem:
        # 해당 가방에 넣을 수 있는 보석이 있음
        result -= heapq.heappop(capable_gem)
        # 그 보석들 중 가장 가치가 큰 보석을 넣음. 마이너스 연산인 이유는 최대힙을 만들기 위해 위 단계에서 가치를 음수로 만들어 넣었기 때문.
        # 이미 최대 힙을 만들어 놓았기 때문에 한번만 꺼내서 써주면 된다.
    elif not jewel:
        # 넣을 수 있는 보석 목록도 원래 보석목록도 없는 경우 반복문 종료
        break

print(result)
