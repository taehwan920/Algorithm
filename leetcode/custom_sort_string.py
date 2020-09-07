class Solution:
    def customSortString(self, S: str, T: str) -> str:
        result = ''
        t = list(T)

        for sam in S:
            idx = 0
            while idx < len(t):
                now = t[idx]
                if now == sam:
                    result += t.pop(idx)
                else:
                    idx += 1

        result += ''.join(t)

        return result
