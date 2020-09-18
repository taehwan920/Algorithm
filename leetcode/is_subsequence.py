class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        s_l = len(s)
        while i < s_l and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == s_l

# 투 포인터 알고리즘의 강력함..
