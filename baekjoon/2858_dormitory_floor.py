import math

r, b = map(int, input().split())
area = r + b
root = int(math.sqrt(area))
factor = []
for i in range(3, root + 1):
    if area % i == 0:
        factor.append((area // i, i))

for fact in factor:
    if b == (fact[0] - 2) * (fact[1] - 2):
        for i in fact:
            print(i, end=" ")
        break

# 이 문제가 완전 탐색인 이유 : 처음에 주어지는 빨간 바닥과 갈색 바닥의 개수가 바닥의 넓이임. -> 바닥 넓이의 약수 짝을 다 구해서 주어진 각 색깔별 바닥의 조건과 일치하는 약수 짝을 찾으면 그게 답.
# 약수 구하는 법 -> 1부터 해당 수의 정수화 시킨 제곱근까지 나눠서 나머지가 0인 수들만 짝지으면 되는데, 이때 나머지가 0일땐 나눈 몫을 같이 짝지어서 배열에 넣어주면 그게 약수 짝이 된다.
# 가장 바깥 테두리가 빨간 바닥이므로 해당 약수 짝에서 각각 2씩 빼줘서 곱한 값이 갈색 바닥의 개수(넓이)와 같으면 문제의 조건이 충족되므로 출력해주면 됨.
