team = {}
for i in range(int(input())):
    player = input()
    if player[0] in team:
        team[player[0]] += 1
    else:
        team[player[0]] = 1
result = []
for i in team:
    if team[i] >= 5:
        result.append(i)

if result:
    result.sort()
    print(''.join(result))
else:
    print('PREDAJA')
