n = int(input())
cards = list(map(int, input().split()))

MAX = max(cards)
cards.pop(cards.index(MAX))
result = MAX * (n-1) + sum(cards)

print(result)
