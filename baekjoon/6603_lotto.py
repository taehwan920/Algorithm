from itertools import combinations
while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    del lotto[0]
    pick = list(combinations(lotto, 6))
    for i in pick:
        for j in i:
            print(j, end=" ")
        print()
    print()
