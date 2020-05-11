n = int(input())

if n == 1:
    print(1)
    exit(0)
if n == 2:
    print(2)
    exit(0)

cache = [0] * 3
cache[0] = 1
cache[1] = 2
count = 2
while count != n:
    cache[2] = cache[1] + cache[0]
    cache[0], cache[1] = cache[1], cache[2]
    count += 1

print(cache[1] % 15746)

# 흔한 dp 피보나치 문제인데, 메모리를 빡빡하게 줘서 memoization의 메모리를 최소화했다.
# dp의 큰 특징은 작은 부분 -> 큰부분으로 확장되는 점화식이 있다는 것과 메모이제이션.
