for _ in range(int(input())):
    cha = list(map(int, input().split()))
    hp = cha[0] + cha[4] if cha[0] + cha[4] > 1 else 1
    mp = cha[1] + cha[5] if cha[1] + cha[5] > 1 else 1
    atk = cha[2] + cha[6] if cha[2] + cha[6] > 0 else 0
    df = cha[3] + cha[7]
    power = hp + 5*mp + 2*atk + 2 * df
    print(power)
