# 소인수분해

N = int(input())
i = 2
while N != 1:
    if N % i == 0:
        N = N / i
        print(i)
    else:
        i += 1

# 나누어 떨어지면 출력. 아니라면 나누는 수를 1씩 증가시켜서 다시 나눈다.
