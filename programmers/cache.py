def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cities = list(map(lambda x: x.upper(), cities))
    q = []
    time = 0
    for i in range(len(cities)):
        if cities[i] in q:
            time += 1
            if len(q) == cacheSize:
                q.pop(q.index(cities[i]))
        else:
            time += 5
            if len(q) == cacheSize:
                q.pop(0)
        q.append(cities[i])
    return time
# 로직에서 크게 틀린건 없었으나 큐 안에 해당 도시가 들어있는 경우 해당 도시를 pop해줘야 했는데 생각없이 pop(0)했던게 패인이었다.
