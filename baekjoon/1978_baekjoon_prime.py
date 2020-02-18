# 소수 판별 문제..
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

T = int(input())
num_li = list(map(int, input().split()))
prime = 0


def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num != 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return True


for j in range(len(num_li)):
    if is_prime(num_li[j]) is True:
        prime += 1
print(prime)
