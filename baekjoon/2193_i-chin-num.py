n = int(input())

cache = [0] * 3
cache[0] = 1
cache[1] = 1
for i in range(2, n):
    cache[2] = cache[0] + cache[1]
    cache[0], cache[1] = cache[1], cache[2]

print(cache[1])
