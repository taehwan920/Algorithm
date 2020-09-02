def is_valid(sss):
    digit = []
    letter = []
    for s in sss:
        if s.isdecimal():
            digit.append(s)
        else:
            letter.append(s)

    if abs(len(digit) - len(letter)) > 1:
        return False
    else:
        return [digit, letter]


def reformat(a, b):
    result = ''
    if len(a) > len(b):
        result += a.pop(0)
        for i in range(len(a)):
            result += b[i]
            result += a[i]
    else:
        for i in range(len(a)):
            result += a[i]
            result += b[i]
    return result


class Solution:
    def reformat(self, s: str) -> str:
        nums = is_valid(s)
        if not nums:
            return ""

        digit, letter = nums
        result = ''

        if len(digit) >= len(letter):
            result = reformat(digit, letter)
        else:
            result = reformat(letter, digit)
        return result
