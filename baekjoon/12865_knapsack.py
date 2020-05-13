n, k = map(int, input().split())

knapsack = [[0]*(k+1) for i in range(n+1)]

for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j >= weight:
            knapsack[i][j] = max(
                knapsack[i-1][j], knapsack[i-1][j-weight] + value)
        else:
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[-1][k])
