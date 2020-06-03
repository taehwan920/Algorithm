n = int(input())
star = input()
l_s = len(star)
to_star = star.index('*')
from_star = -1 * (l_s - (to_star + 1))
for i in range(n):
    temp = input()
    if temp == "" or len(temp) < len(star[:to_star]) + len(star[from_star:]):
        print('NE')
        continue
    if temp[:to_star] == star[:to_star] and temp[from_star:] == star[from_star:]:
        print('DA')
    else:
        print('NE')

# 입력값이 a*a, a 일때 da를 출력해버려서 틀렸었음. 그래서 길이가 별을 제외한 star 문자열의 길이보다 짧을 경우 ne로 빠지도록 함.
