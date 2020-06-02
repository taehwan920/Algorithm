result = 0
last = -1
for i in range(10):
    last = int(input())
    result += last
    if result >= 100:
        break

if result < 100:
    print(result)
elif result == 100:
    print(100)
else:
    temp = result - last
    if 100 - temp >= result - 100:
        print(result)
    else:
        print(temp)

# 10개의 버섯을 다 먹어도 100이 안넘는 케이스 출력을 구현하지 않아서 틀렸음.
