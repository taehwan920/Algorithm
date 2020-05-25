h, m = map(int, input().split())
cook = int(input())

total = h * 60 + m + cook
new_h = (total // 60) % 24
new_m = total % 60
print(new_h, new_m)
