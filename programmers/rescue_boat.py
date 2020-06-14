def solution(people, limit):
    n = len(people)
    if n == 1:
        return 1
    people.sort()
    cnt = 0
    for i in range(n):
        if people[i] == limit + 1:
            continue
        cnt += 1
        boat = people[i]
        for j in range(n-1, i, -1):
            if boat + people[j] <= limit:
                people[j] = limit + 1
                break
    return cnt

# 직접 풀이한것. 정확성은 다 정답처리되었으나 효율성 테스트에서 전부 시간초과가 떴음.


def solution1(people, limit):
    p = sorted(people, reverse=True)
    answer = len(p)
    s, e = 0, len(p) - 1
    while s < e:
        if p[s] + p[e] <= limit:
            e -= 1
            answer -= 1
        s += 1
    return answer

# 다른사람의 풀이. 내 풀이와 비교해보면 나는 반복문으로 작은값을 선택한 뒤 반복문을 하나 더 사용하여 뒤에서부터 값을 확인해 현재 선택된 작은값과 더해서 limit보다 적으면 해당 값을 사용못하도록한 뒤
# 반복문을 탈출하는 식으로 답을 구했음
# 다른 사람의 풀니는 기본적으로 1인당 보트를 한번씩 탄다고 가정을 해두고, 큰값부터 보면서 아직 보트에 안 탄 값 중 가장 작은값을 더해보고 그게 limit보다 작으면 보트탄 횟수를 하나씩 차감하는 식으로 했다.
# 생각해보면 작은값부터 체크하면 뒤에서부터 계속 반복문 돌면서 봐야하는데 큰값부터 보면 가장 작은값을 더해서 limit와 비교해보기만 하면되니 시간복잡도가 O(n)으로 줄어들수있었다.
