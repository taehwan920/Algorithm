class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxrows = [0] * n
        maxcols = [0] * n

        for i in range(n):
            max_r = 0
            max_c = 0
            for j in range(n):
                now_r = grid[i][j]
                now_c = grid[j][i]
                if now_r > max_r:
                    max_r = now_r
                if now_c > max_c:
                    max_c = now_c
            maxrows[i] = max_r
            maxcols[i] = max_c

        result = 0
        for i in range(n):
            for j in range(n):
                now = grid[i][j]
                result += min(maxrows[i], maxcols[j]) - now

        return result
