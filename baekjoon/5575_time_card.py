a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
all_a = a[3] * 3600 + a[4] * 60 + a[5] - (a[0] * 3600 + a[1] * 60 + a[2])
all_b = b[3] * 3600 + b[4] * 60 + b[5] - (b[0] * 3600 + b[1] * 60 + b[2])
all_c = c[3] * 3600 + c[4] * 60 + c[5] - (c[0] * 3600 + c[1] * 60 + c[2])
print(all_a // 3600, (all_a % 3600) // 60, (all_a % 3600) % 60)
print(all_b // 3600, (all_b % 3600) // 60, (all_b % 3600) % 60)
print(all_c // 3600, (all_c % 3600) // 60, (all_c % 3600) % 60)
