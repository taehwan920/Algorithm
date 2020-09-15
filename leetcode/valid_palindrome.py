class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in range(len(s)):
            if s[i].isalpha():
                temp.append(s[i].lower())
            if s[i].isdecimal():
                temp.append(s[i])

        s_temp = ''.join(temp)
        return s_temp == s_temp[::-1]
