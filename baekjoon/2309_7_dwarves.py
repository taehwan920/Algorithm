from itertools import combinations

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

perm = list(combinations(dwarf, 7))
perm = list(filter(lambda x: sum(x) == 100, perm))
ans = sorted(perm[0])
for i in ans:
    print(i)

# permutations = 순열 = 내용은 같아도 순서가 다른 것까지 전부 뽑음
# combinations = 조합 = 내용이 같으면 뽑지 않음
