import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


class Result:
    val = 0


for _ in range(int(input())):
    Result.val = 0
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [True] + [False for i in range(n)]

    def dfs(num):
        visited[num] = True
        cycle.append(num)
        want = students[num]

        if visited[want]:
            if want in cycle:
                Result.val += len(cycle[cycle.index(want):])
            return
        else:
            dfs(want)

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - Result.val)

# 사이클 확인을 cycle 배열을 만들어서 넣어 두고 만약 이미 들어가 있는게 또 나오는 경우 사이클로 판정함. 그래서 해당 사이클 길이만큼만 더하는 걸로 해결..
