from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        l = len(arr)
        visited = [0 for i in range(l)]

        while q:
            now = q.popleft()
            if arr[now] == 0:
                return True

            steps = [now - arr[now], now + arr[now]]
            for step in steps:
                if 0 <= step < l and visited[step] == 0:
                    q.append(step)
                    visited[step] = 1

        return False
