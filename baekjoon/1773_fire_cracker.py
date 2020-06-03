n, c = map(int, input().split())
fire_cracker = [False for i in range(c+1)]
for i in range(n):
    student = int(input())
    time = student
    while time <= c:
        if not fire_cracker[time]:
            fire_cracker[time] = True
        time += student

print(fire_cracker.count(True))
