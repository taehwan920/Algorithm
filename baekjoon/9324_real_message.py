def is_real(string):
    string = list(string)
    alpha = [0 for i in range(26)]
    jump = 0
    for i in range(len(string)):
        if jump:
            jump -= 1
            continue
        letter = ord(string[i]) - ord('A')
        alpha[letter] += 1
        if alpha[letter] % 3 == 0:
            if i == len(string) - 1:
                return False
            elif string[i+1] != string[i]:
                return False
            else:
                jump = 1
    return True


for _ in range(int(input())):
    temp = input()
    if is_real(temp):
        print('OK')
    else:
        print('FAKE')
# 해당 글자까지 세서 글자 수가 3의 배수인데도 뒤에 같은 글자가 없거나 해당 글자가 마지막 글자일 경우 False를 리턴하도록 해서 판별하는 코드를 짰다.
