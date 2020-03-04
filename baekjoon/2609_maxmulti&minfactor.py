a, b = map(int, input().split())

c, d = max(a, b), min(a, b)
t = 1
while t != 0:
    t = c % d
    c, d = d, t

print(c)
print(int(a*b/c))

# 최대 공약수 구하는 공식을 반드시 숙지해둘 것. 그리고 정수값 도출해야 할때는 웬만하면 int 걸어서 할것
