# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# 첫번째 답
A, B, V = map(int, input().split())

height = 0
days = 0
while V > height:
    days += 1
    height += A
    if V <= height:
        break
    height -= B

print(days)
# 단순하게 생각해서 문제그대로 반복문으로 작성했으나 시간초과로 오답.

# 두번째 답
A, B, V = map(int, input().split())

days = (V - A) // (A - B) + 1

print(days)

# 세번째 답

A, B, V = map(int, input().split())

if (V - B) % (A - B) != 0:
    days = ((V - B) // (A - B)) + 1
else:
    days = (V - B) // (A - B)

print(days)
# 정답. 결국 내 힘으로는 못풀었음. 정상에 도달하면 미끄러지지 않는다고했으니 결국 올라가야할 높이는 V-B만큼이었던것.
