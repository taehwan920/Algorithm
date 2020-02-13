# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.


def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        if a < b:
            for i in range(a, b+1):
                answer += i
        elif a > b:
            for i in range(b, a+1):
                answer += i
    return answer
# 조건을 잘읽어보고 풀어야한다는 걸 잊지 말 것
# 다른사람의 풀이


def adder(a, b):
    if a > b:
        a, b = b, a

    return sum(range(a, b+1))
# a가 b 보다 클땐 a, b를 각각 b, a로 재설정해서 무조건 큰게 b로 가도록 몰아서 sum함수로 리턴했다.
