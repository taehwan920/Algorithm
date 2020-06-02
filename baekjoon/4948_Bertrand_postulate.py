MAX = 246912
prime = [False, False] + [True for i in range(MAX + 1)]
for idx, num in enumerate(prime):
    if num:
        k = idx * 2
        while k <= MAX:
            prime[k] = False
            k += idx

while True:
    n = int(input())
    if n == 0:
        break
    print(prime[n+1:2*n+1].count(True))
