from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = deque([[sr, sc]])
        w, h = len(image[0]), len(image)
        start = image[sr][sc]
        image[sr][sc] = newColor
        visited = [[0 for i in range(w)] for i in range(h)]
        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while q:
            y, x = q.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    continue
                if image[ny][nx] != start or visited[ny][nx] == 1:
                    continue
                visited[ny][nx] = 1
                image[ny][nx] = newColor
                q.append([ny, nx])

        return image
