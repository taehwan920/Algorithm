class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        if n == 0:
            return s
        result = ['' for i in range(n)]

        for idx, num in enumerate(indices):
            result[num] = s[idx]

        return ''.join(result)
