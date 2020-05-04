from itertools import permutations


def solution(numbers):
    answer = set()  # 반복 제거를 위한 set 자료형
    maximum = 10 ** 7  # 숫자 최대 길이가 7글자이므로
    prime_li = [False, False] + [True] * maximum  # index로 소수 판별하기 위해서
    for i, num in enumerate(prime_li):  # enumerate는 인덱스와 밸류를 한번에 보여줌
        if num:
            k = i*2
            while k <= maximum:
                prime_li[k] = False  # num이 소수면 그 배수는 싹 다 False이므로 그 작업.
                k += i

    for i in range(1, len(numbers)+1):
        perm = permutations(list(numbers), i)  # 순열 모듈인 permutations
        for i in list(perm):
            num = int("".join(list(i)))  # 튜플인 자료형을 리스트로 바꾸고 join으로 붙여서 int로.
            if prime_li[num]:
                answer.add(num)
    return len(answer)
