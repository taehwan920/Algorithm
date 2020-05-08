N = int(input())

users = []
for i in range(N):
    age, name = input().split()
    users.append((int(age), name))

_users = sorted(users, key=lambda x: x[0])

for i in _users:
    print(i[0], i[1])
