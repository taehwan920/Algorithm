def solution(dirs):
    visited = []
    control = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    nx, ny = 5, 5
    count = 0
    for con in dirs:
        move = control[con]
        now = [ny, nx]
        new = [ny + move[0], nx + move[1]]
        if 0 <= new[0] <= 10 and 0 <= new[1] <= 10:
            if (now, new) not in visited:
                visited.append((now, new))
                visited.append((new, now))
                ny, nx = new[0], new[1]
                count += 1
            else:
                ny, nx = new[0], new[1]
    return count

# 문자열을 통해 일일이 들어오는 조작은 dict로 해결.
# 과거 방문 여부가 이동 횟수 계산에 영향을 주기 때문에 visited에다 이동했던 좌표를 짝을 지어 넣어두는데, 이때 좌표쌍의 순서를 바꾸어서 하나 더 넣는다. 왜냐면 같은 좌표를 통해 다시 돌아오는 경우도 체크해야함.
# 이건 원래 set 자료형으로 해결하려고 했으나 set자료형은 배열이 요소로 들어갈 수 없기 때문에 튜플로 쌍을 지어 visited에 넣어 두었다.
