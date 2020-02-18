# 네 번째 점

# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

if b[0] == c[0]:
    d_x = a[0]
elif a[0] == c[0]:
    d_x = b[0]
elif a[0] == b[0]:
    d_x = c[0]

if b[1] == c[1]:
    d_y = a[1]
elif a[1] == c[1]:
    d_y = b[1]
elif a[1] == b[1]:
    d_y = c[1]

print(f'd_x d_y')
