class Solution:
    def reverseWords(self, s: str) -> str:
        s_ = s.split(' ')

        for i in range(len(s_)):
            s_[i] = s_[i][::-1]

        return ' '.join(s_)
