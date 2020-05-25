import sys
s1 = sys.stdin.readline()
s2 = sys.stdin.readline()
if len(s1) > len(s2):
    s1, s2 = s2, s1
l_s1 = len(s1) - 1

longest = 0
for i in range(l_s1):
    for j in range(1, l_s1-i+1):
        if len(s1[i:i+j]) > longest:
            if s1[i:i+j] in s2:
                longest = len(s1[i:i+j])
            else:
                break
print(longest)

# 메모이제이션을 리스트로 했더니 시간초과가 떠서 변수 저장식으로 바꿔서 통과했다.
