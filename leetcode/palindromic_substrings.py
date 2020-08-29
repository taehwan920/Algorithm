class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                temp = s[j:j+i]
                if temp == temp[::-1]:
                    cnt += 1
        return cnt
