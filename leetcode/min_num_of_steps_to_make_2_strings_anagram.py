class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_arr = [0 for i in range(26)]
        t_arr = [0 for i in range(26)]

        for i in range(len(s)):
            now_s = ord(s[i])
            now_t = ord(t[i])
            a = ord('a')
            s_arr[now_s - a] += 1
            t_arr[now_t - a] += 1

        how_many = 0

        for i in range(26):
            if s_arr[i] > t_arr[i]:
                how_many += s_arr[i] - t_arr[i]

        return how_many
