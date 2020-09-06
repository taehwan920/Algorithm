def is_small(s):
    if ord('a') <= ord(s) <= ord('z'):
        return True
    else:
        return False


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if is_small(word[0]):
            for i in range(1, len(word)):
                if not is_small(word[i]):
                    return False
            return True
        else:
            caps = 1
            for i in range(1, len(word)):
                if not is_small(word[i]):
                    caps += 1
            if caps == 1 or caps == len(word):
                return True
            else:
                return False
