def solution(B, M):
    M = list(map(lambda x: x - 1, M))
    moved = [0]
    count = 0
    for i in M:
        for j in range(len(B)):
            craned = B[j][i]
            if craned != 0:
                if moved[-1] == craned:
                    B[j][i] = 0
                    moved.pop()
                    count += 2
                    break
                else:
                    moved.append(craned)
                    B[j][i] = 0
                    break
    return count
