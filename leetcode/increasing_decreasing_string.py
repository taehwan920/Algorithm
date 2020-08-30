class Solution:
    def sortString(self, s: str) -> str:
        s_arr = sorted(list(s))
        small_mode = True
        result = ''
        last = 0
        while s_arr:
            if small_mode:
                for idx in range(len(s_arr)):
                    if ord(s_arr[idx]) > last:
                        this = s_arr.pop(idx)
                        result += this
                        last = ord(this)
                        break
                else:
                    last = 1e9
                    small_mode = False
            else:
                for idx in reversed(range(len(s_arr))):
                    if ord(s_arr[idx]) < last:
                        this = s_arr.pop(idx)
                        result += this
                        last = ord(this)
                        break
                else:
                    last = 0
                    small_mode = True

        return result
