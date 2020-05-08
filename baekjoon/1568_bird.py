n = int(input())

k = 1
count = 0

while n > 0:
    count += 1
    if n < k:
        k = 1
    n -= k
    k += 1

print(count)
