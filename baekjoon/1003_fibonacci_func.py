t = int(input())

for _ in range(t):
    num = int(input())
    mem = [[1, 0], [0, 1], [1, 1]]
    if num == 0:
        print(mem[0][0], mem[0][1])
    elif num == 1:
        print(mem[1][0], mem[1][1])
    elif num == 2:
        print(mem[2][0], mem[2][1])
    else:
        for i in range(3, num+1):
            mem[0], mem[1] = mem[1], mem[2]
            mem[2] = [mem[0][0]+mem[1][0], mem[0][1]+mem[1][1]]
        print(mem[2][0], mem[2][1])
