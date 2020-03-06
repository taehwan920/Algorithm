STR = list(input())

i = 0
letter = 0

while i < len(STR):
    if (STR[i] == "c" and STR[i+1] == "-"):
        i += 2
        letter += 1
    elif (STR[i] == "c" and STR[i+1] == "="):
        i += 2
        letter += 1
    elif STR[i] == "d" and STR[i+1] == "z" and STR[i+2] == "=":
        i += 3
        letter += 1
    elif STR[i] == "d" and STR[i+1] == "-":
        i += 2
        letter += 1
    elif STR[i] == "l" and STR[i+1] == "j":
        i += 2
        letter += 1
    elif STR[i] == "n" and STR[i+1] == "j":
        i += 2
        letter += 1
    elif STR[i] == "s" and STR[i+1] == "=":
        i += 2
        letter += 1
    elif STR[i] == "z" and STR[i+1] == "=":
        i += 2
        letter += 1
    else:
        i += 1
        letter += 1

print(letter)
# 내가 푼 방식 : 전부 조건식으로 해결했음.

# 다른사람이 푼 방식

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = input()

for t in a:
    alpha = alpha.replace(t, '*')

print(len(alpha))

# 조건을 전부 배열로 정리해서 저것에 해당하는 문자열을 임의 한 글자 문자열로 대체한 뒤 길이를 구했다. 이쪽이 훨씬 수정하기도 쉬운듯.
