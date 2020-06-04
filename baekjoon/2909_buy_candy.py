candy, log = map(int, input().split())


def int_round(num, log):
    this = num % (10 ** (log + 1))
    # 해당 자리수까지만 남기고 앞에 붙은 수들은 다 쳐내기 ex ) 149, 2가 들어오면 49만 남기기.
    bigger = (num // (10 ** (log + 1))) * (10 ** (log + 1))
    # 해당 자리수보다 더 큰 수를 일단 준비해둠 ex ) 149, 2가 들어오면 100을 bigger에 저장해둠
    if this >= 5 * (10 ** log):
        # 저장해둔 this에서 반올림해야하는 자리의 숫자만 체크.
        return bigger + 10 ** (log + 1)
    else:
        return bigger


if log == 0:
    print(candy)
else:
    print(int_round(candy, log - 1))
# 이 문제는 파이썬 내장 함수 round를 써서는 풀 수 없는 문제.
# 왜냐면 파이썬 round는 만일 반올림 해야하는 자리의 수가 5일 경우 조금이라도 더 가까운 짝수로 올리거나 내리는 식임.
# 예를 들어 1.5를 반올림하면 2가되고 2.5를 반올림하면 3이 되는게 아닌 가장 가까운 짝수인 2가 되어버림. 2.6부터는 3이되는 식임.
# 그래서 직접 반올림 함수를 작성해야했다.
