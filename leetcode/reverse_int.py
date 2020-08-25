class Solution:
    def reverse(self, x: int) -> int:
        pos = True if x >= 0 else False
        temp = list(str(abs(x)))
        temp.reverse()
        result = int(''.join(temp)) if pos else -1 * int(''.join(temp))
        result = result if -1 * (2 ** 31) <= result < 2 ** 31 else 0
        return result

# 32비트 범위를 초과하는 숫자는 0으로 처리하라는 조건을 간과해서 틀렸음. 문제를 꼼꼼히.. 제발
