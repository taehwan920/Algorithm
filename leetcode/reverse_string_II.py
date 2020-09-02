class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]

        for i in range(0, len(s), 2 * k):
            temp = s[i:i+k]
            s = s[:i] + temp[::-1] + s[i+k:]

        return s
