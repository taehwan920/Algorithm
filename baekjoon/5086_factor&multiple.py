# 배수와 약수

# 문제
# 4 × 3 = 12이다.

# 이 식을 통해 다음과 같은 사실을 알 수 있다.

# 3은 12의 약수이고, 12는 3의 배수이다.

# 4도 12의 약수이고, 12는 4의 배수이다.

# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

# 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

# 예제 입력 1
# 8 16
# 32 4
# 17 5
# 0 0

# 예제 출력 1
# factor
# multiple
# neither

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
