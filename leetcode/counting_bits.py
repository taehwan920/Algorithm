class Solution:
    def countBits(self, num: int) -> List[int]:
        def to_bin(n):
            temp = 0
            while n:
                if n % 2 == 1:
                    temp += 1
                n //= 2
            return temp

        result = [0 for i in range(num + 1)]

        for i in range(num+1):
            result[i] = to_bin(i)

        return result
