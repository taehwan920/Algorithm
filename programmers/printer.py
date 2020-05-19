def solution(priorities, location):
    queue = [(doc, i) for i, doc in enumerate(priorities)]
    count = 1
    while True:
        if queue[0][0] == max(priorities):
            priorities[priorities.index(max(priorities))] = 0
            if queue[0][1] == location:
                return count
            queue.pop(0)
            count += 1
        else:
            queue.append(queue.pop(0))

# 간단하게 구현만 하면 되는 문제였음. 너무 어렵게 생각하지 말 것.
# 구현 도중 요소 위치가 이리 저리 바귀는데 원래 인덱스를 구해야하는 문제의 경우 처음 인덱스를 포함하고 있는 자료 형태로 바꿔서 구현을 하면 된다.
