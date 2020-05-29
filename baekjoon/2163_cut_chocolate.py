n, m = map(int, input().split())
n, m = min(n, m), max(n, m)

print((n-1) + n * (m - 1))
