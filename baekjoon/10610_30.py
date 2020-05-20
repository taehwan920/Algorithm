n = input()

if '0' not in n:
    print(-1)
    exit(0)

temp = 0
for i in n:
    temp += int(i)

if temp % 3 != 0:
    print(-1)
    exit(0)

n = sorted(list(n), key=lambda x: x, reverse=True)
print(int(''.join(n)))

# 각 자리수를 더한 것이 3의 배수이며, 0이 들어있는 수가 30의 배수의 조건.
# 그래서 0이 없는것 경우 or 각 자리수를 더한 것이 3의 배수가 아닌 경우 -1을 출력한다.
# 모든 자릿수의 합이 3의 배수이기만 하면되니 무조건 큰 수가 앞으로 오도록 정렬해서 int로 만들어 준 뒤 출력하면 된다.
