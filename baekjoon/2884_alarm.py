h, m = map(int, input().split())
total = h*60 + m - 45 if h*60 + m - 45 > 0 else h*60 + m - 45 + (24 * 60)
result_h, result_m = total // 60, total % 60
if result_h == 24:
    result_h = 0

print(result_h, result_m)
