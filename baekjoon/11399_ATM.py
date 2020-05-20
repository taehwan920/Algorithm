n = int(input())

men = list(map(int, input().split(' ')))
men.sort()
result = 0
for i in range(n):
    result += sum(men[:i+1])

print(result)

# ATM에서 돈을 뽑기 위해 줄을 선 사람들이 모두 돈을 뽑는데 걸리는 가장 짧은시간.
# 시간이 적게 걸리는 사람부터 뽑아야 적게 걸림. 왜냐면 앞사람이 뽑는데 걸린 시간만큼 계속 기다려야하므로.
# 그래서 오름차순으로 정렬한 뒤 각 인덱스 별로 해당 인덱스까지의 요소의 합을 전부 더해주면 답이 나온다.
