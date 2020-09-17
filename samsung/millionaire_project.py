import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    prices.reverse()

    result = 0
    accum = 0
    biggest = prices[0]
    for i in range(n):
        if prices[i] > biggest:
            result += accum
            accum = 0
            biggest = prices[i]
        else:
            accum += biggest - prices[i]
    result += accum
    print(f'#{t+1} {result}')
