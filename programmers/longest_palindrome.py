def solution(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            temp = s[i:j]
            if temp == temp[::-1]:
                l = len(temp)
                longest = l if l > longest else longest
    return longest
