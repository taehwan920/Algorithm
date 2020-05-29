n, m = map(int, input().split())
brand = [1000, 1000]
for _ in range(m):
    new6, new1 = map(int, input().split())
    brand[0] = min(brand[0], new6)
    brand[1] = min(brand[1], new1)


def string6(num):
    temp = n // 6 if n % 6 == 0 else (n // 6) + 1
    return temp * num


result = min(string6(brand[0]), n * brand[1],
             (n // 6) * brand[0] + (n % 6) * brand[1])
print(result)

# 각 브랜드 별로 가장 싼 기타줄만 모아서 그중 가장 비용이 적게드는걸 출력하면 된다.
