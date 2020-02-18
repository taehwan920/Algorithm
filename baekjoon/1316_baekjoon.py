rep = int(input())
nums = 0


def is_group(s):
    if len(s) == 1:
        return True
    black_list = []
    last_chr = s[0]
    for i in range(1, len(s)):
        if s[i] in black_list:
            return False
        if s[i] != last_chr:
            black_list.append(last_chr)
            last_chr = s[i]
    return True


for j in range(rep):
    word = input()
    if is_group(word) is True:
        nums += 1
print(nums)
