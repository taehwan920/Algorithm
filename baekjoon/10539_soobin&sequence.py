n = int(input())
sequence = list(map(int, input().split()))
accum = 0
new_seq = []
for i in range(len(sequence)):
    temp = sequence[i] * (i+1)
    now = temp - accum
    new_seq.append(now)
    accum += now

for i in new_seq:
    print(i, end=" ")
