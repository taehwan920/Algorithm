def solution(B, M):
    stack = []
    moves = list(map(lambda x: x - 1, M))
    result = 0
    for move in moves:
        for i in range(len(B)):
            now = B[i][move]
            if now != 0:
                B[i][move] = 0
                if stack and stack[-1] == now:
                    stack.pop()
                    result += 2
                else:
                    stack.append(now)
                break
    return result

# 전에 풀었던거 다시 풀었음. 반복문 탈출조건 중요.
