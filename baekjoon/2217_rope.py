n = int(input())

ropes = []
dp = [0] * n

for i in range(n):
    ropes.append(int(input()))
ropes.sort()

for i in range(n):
    dp[i] = ropes[i] * (n - i)

print(max(dp))
# 그리디 알고리즘이지만 dp로 풀었다. 굳이 순서가 상관없는 문제의 경우 해당 요소보다 큰건 배열의 길이와 인덱스 만으로 시간 복잡도를 늘리지 않고 범위를 지정할 수 있으므로 잊지말자.

n = int(input())
ropes = []

for i in range(n):
    ropes.append(int(input()))
ropes.sort()

biggest = 0
for i in range(n):
    biggest = max(biggest, ropes[i] * (n - i))

print(biggest)
# 그리디 알고리즘으로 푼 사람의 논리 구조대로 한번 풀어봤다. memoization이 아닌 당장 제일 큰 값만 저장하는 변수를 사용해서 풀어봤는데 소요시간은 dp쪽이 훨씬 짧았다.
