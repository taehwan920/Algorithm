n, m = map(int, input().split())


class bar:
    L = 1
    R = m


cnt = 0
for i in range(int(input())):
    apple = int(input())
    if apple < bar.L:
        dist = bar.L - apple
        bar.L -= dist
        bar.R -= dist
        cnt += dist
    elif bar.R < apple:
        dist = apple - bar.R
        bar.L += dist
        bar.R += dist
        cnt += dist

print(cnt)
