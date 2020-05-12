days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())

for i in range(m):
    d += month[i]

print(days[d % 7])
