t = int(input())

prime = [False] * 2 + [True for i in range(99)]
for idx, num in enumerate(prime):
    if num:
        k = idx * 2
        while k <= 100:
            prime[k] = False
            k += idx
factors = [2 for i in range(101)]
factors[0], factors[1] = 0, 1

for i in range(4, 101):
    if prime[i]:
        continue
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    factors[i] = cnt

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if factors[i] % 2 != 0:
            cnt += 1
    print(cnt)
