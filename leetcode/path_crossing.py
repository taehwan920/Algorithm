class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {
            'N': (-1, 0),
            'S': (1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }
        visited = [[0, 0]]
        now = [0, 0]

        for move in path:
            print(now)
            dy, dx = direction[move]
            new = [now[0] + dy, now[1] + dx]
            if new in visited:
                return True
            visited.append(new)
            now = new

        return False
