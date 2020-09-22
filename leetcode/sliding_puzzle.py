def get_state(arr):
    temp = list(map(str, arr))
    return ''.join(temp)


def get_zero_pos(s):
    for i in range(6):
        if s[i] == "0":
            return i


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        direction = {0: [1, 3], 1: [0, 2, 4], 2: [
            1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        temp = []
        for i in range(2):
            temp.extend(board[i])
        state = get_state(temp)

        if state == '123450':
            return 0

        visited = {}
        visited[state] = 1
        start = [0, state, get_zero_pos(state)]
        q = [start]

        while q:
            step, now, z_i = q.pop(0)
            if now == '123450':
                return step
            for _move in direction[z_i]:
                new = ''
                if _move < z_i:
                    new = now[:_move] + '0' + now[_move+1:z_i] + \
                        now[_move] + now[z_i+1:]
                else:
                    new = now[:z_i] + now[_move] + \
                        now[z_i+1:_move] + '0' + now[_move+1:]
                if visited.get(new):
                    continue
                visited[new] = 1
                q.append([step + 1, new, _move])
        return -1

# 부등호 방향 하나 잘못 써서 시간 엄청 잡아먹음
# 배열 크기가 작으므로 아예 문자열로 변환시켜서 상태를 저장하고, 그 상태를 dict를 사용해 visited 판별하여 찾도록함
# 0가 위치를 옮길 인덱스가 현재 위치보다 큰가 작은가에 따라서도 문자열 만드는 방법이 살짝 달라지게해야 문자열 편집이 제대로 됨
