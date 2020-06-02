import math
n = int(input())
log = int(math.log10(n))
remain = n - 10 ** log + 1
result = 0
for i in range(log):
    result += 9 * (10 ** i) * (i + 1)
result += remain * (log + 1)
print(result)
