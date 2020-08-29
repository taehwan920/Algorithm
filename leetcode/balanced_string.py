class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        stack = []
        for let in s:
            if len(stack) == 0:
                count += 1
                stack.append(let)
            else:
                if stack[-1] != let:
                    stack.pop()
                else:
                    stack.append(let)

        return count
