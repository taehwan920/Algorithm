class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)

        if n == 0:
            return True

        score = {'A': 0, 'L': 0, 'P': 0}

        for c in s:
            if score['L'] > 2 or score['A'] > 1:
                return False
            if c != 'L':
                score['L'] = 0
            score[c] += 1

        if score['L'] > 2 or score['A'] > 1:
            return False
        return True
