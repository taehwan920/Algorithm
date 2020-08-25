class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ori = str(x)
        rev = list(str(x))
        rev.reverse()

        for i in range(len(ori)):
            if ori[i] != rev[i]:
                return False
        return True
