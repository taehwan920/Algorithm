class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def sanitize(s):
            temp = ''
            skip = 0
            for i in reversed(range(len(s))):
                if s[i] == "#":
                    skip += 1
                    continue
                if skip:
                    skip -= 1
                    continue
                temp += s[i]

            return temp[::-1]

        return sanitize(S) == sanitize(T)
