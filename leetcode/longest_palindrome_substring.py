class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(result) >= j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    result = s[i:j]
                    break
        return result
