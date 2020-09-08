class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        par = []

        for idx, let in enumerate(s):
            if let == "(":
                stack.append(idx)
                par.append('(')
            if let == ")":
                if par and stack:
                    if par[-1] == "(":
                        par.pop()
                        stack.pop()
                        continue
                stack.append(idx)
                par.append(')')

        result = ''
        for i in range(len(s)):
            if i in stack:
                continue
            result += s[i]

        return result
