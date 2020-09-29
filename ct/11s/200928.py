# 1


def solution(S):
    n = len(S)
    cnt_a = 0
    not_a = 0

    for i in range(n):
        if cnt_a == 3:
            return -1
        if S[i] == 'a':
            cnt_a += 1
        else:
            not_a += 1
            cnt_a = 0

    add_a = 2 * (not_a + 1)
    num_a = n - not_a

    result = add_a - num_a
    return result

# a는 a가 아닌 글자들의 개수에 따라 컨트롤됨. 연속된 a가 3개를 넘지않게 주어진 문자열이라면 일단 a가 아닌 문자열에 a를 붙이는 수를 계산한 다음 a의 개수만큼 a를 빼면 됨

# 2


def solution(S):
    n = len(S)
    m = len(S[0])

    check = {}

    for i in range(n):
        for j in range(m):
            now = S[i][j]
            if not check.get(j):
                check[j] = {}
            if not now in check[j]:
                check[j][now] = i
            else:
                return [check[j][now], i, j]

    return []
# 처음에 n^2 * m으로 풀었다가 이건 아닌것같아서 dict형으로 문제 다시 풂.
# 각 자리 별로 비교해서 있는지 없는지 체크하고, 만약 있으면 해당 글자에 먼저 저장된 단어의 인덱스와 현재 단어의 인덱스, 그리고 몇번째 글자인지 나타내는 숫자를 같이 리턴함

# 3


def solution(A):
    n = len(A)

    total = n * (n+1) // 2
    real_sum = sum(A)

    result = abs(total - real_sum)

    return result if result <= 10 ** 9 else -1

# 각 요소가 전부 다른 배열이 주어지고 거기서 중간에 빠진 수를 찾는 문제랑 굉장히 흡사해서 그거 응용함
# 각 요소가 전부 다른 배열이 주어지는걸 확인하려면
