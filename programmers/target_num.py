def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return sup.count(target)

# 어렵게 탐색할 필요없이 구현으로 끝나는 문제였다..
# 0을 시작으로 number의 요소를 빼주면 됐음. bfs의 변형.
