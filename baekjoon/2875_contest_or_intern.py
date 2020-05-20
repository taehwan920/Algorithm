n, m, k = map(int, input().split())

contest = 0
while n+m >= k+3 and n > 1 and m > 0:
    n -= 2
    m -= 1
    contest += 1

print(contest)


# 그리디라기보단 구현 문제.
# 반복문 조건이 n+m >= k 일 경우 한 번 더 진행이 돼서 k 보다 작아졌을 경우 contest 를 하나 빼줘야 하는데
# 혹시 n이나 m이 0으로 입력 된 경우 contest를 빼주면 음수값이 돼버려서 귀찮아지므로 k + 3으로 조건을 잡아줘서 굳이 추가적으로 해주지 않아도 됨.
