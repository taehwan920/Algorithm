class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000: return str(n)
        
        num = str(n)
        
        cnt = 0
        r_arr = []
        for i in reversed(range(len(num))):
            if cnt == 3:
                cnt = 0
                r_arr.append('.')
            r_arr.append(num[i])
            cnt += 1
        
        r_arr.reverse()
        return ''.join(r_arr)