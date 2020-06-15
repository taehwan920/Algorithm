def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def solution(n, k):
    nums = [i for i in range(1, n+1)]
    result = []

    def recur(num, kk):
        if num == 1:
            result.append(nums[kk])
        else:
            total = factorial(num)
            divider = total // num
            new_kk = kk % divider
            num_order = kk // divider if new_kk else kk // divider - 1
            if num_order < 0:
                num_order = 0
            result.append(nums[num_order])
            nums.pop(num_order)
            recur(num - 1, new_kk)
    recur(n, k)
    return result

# 처음 풀이. 정확도가 조금 떨어짐. 다시 풀어봐야겠다.


def solution1(n, k):
    nums = [i for i in range(1, n+1)]
    result = []
    while n > 0:
        temp = factorial(n) // n
        idx = k // temp
        k = k % temp
        if k:
            result.append(nums.pop(idx))
        else:
            result.append(nums.pop(idx - 1))
        n -= 1
    return result

# 내가 구현능력이 조금 떨어져서 틀렸다.
# 팩토리얼(해당 순열의 개수)을 n으로 나누어 그 몫과 나머지에 따라 오는 숫자가 달라지고, 그걸 활용해 풀기만 하면 됐는데 거기부터 갑자기 머리가 복잡해져서 이것저것 헷갈려서 틀리게 된 듯하다.
# 연습장 혹은 편집기에 로직을 쭉 써보고 풀어야 좀 더 정확하게 문제를 풀 수 있겠다.
