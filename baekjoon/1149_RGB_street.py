n = int(input())

prices = []

for _ in range(n):
    rgb = list(map(int, input().split()))
    prices.append(rgb)


houses = [[0]*3 for i in range(n)]
houses[0][0] = prices[0][0]
houses[0][1] = prices[0][1]
houses[0][2] = prices[0][2]

for i in range(1, len(prices)):
    houses[i][0] = prices[i][0] + min(houses[i-1][1], houses[i-1][2])
    houses[i][1] = prices[i][1] + min(houses[i-1][0], houses[i-1][2])
    houses[i][2] = prices[i][2] + min(houses[i-1][0], houses[i-1][1])

print(min(houses[-1]))
