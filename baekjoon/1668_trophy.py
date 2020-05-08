N = int(input())

prizes = []

for i in range(N):
    prizes.append(int(input()))

highest = prizes[0]
l_count = 1
for i in range(1, len(prizes)):
    if highest < prizes[i]:
        highest = prizes[i]
        l_count += 1

highest = prizes[-1]
r_count = 1
for i in range(len(prizes) - 2, -1, -1):
    if highest < prizes[i]:
        highest = prizes[i]
        r_count += 1

print(l_count)
print(r_count)
