class Solution:
    def toLowerCase(self, str: str) -> str:
        lowers = [chr(i) for i in range(ord('a'), ord('z')+1)]

        s_arr = list(str)
        for i in range(len(s_arr)):
            temp = ord(s_arr[i])
            if ord('a') <= temp <= ord('z'):
                continue
            if ord('A') <= temp <= ord('Z'):
                s_arr[i] = lowers[temp - ord('A')]

        return ''.join(s_arr)
