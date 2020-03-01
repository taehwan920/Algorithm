T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, (input().split())))
    order = 0
    if N == 1:
        print(1)
    else:
        for j in range(N-1, M, -1):  # 배열의 맨 뒤부터 해당 문서까지 비교해보며
            if queue[M] <= queue[j]:
                order += 1
        print(order)


case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    print_list = list(map(int, input().split()))
    prior_number = []

    # 우선 순위를 탐색하기 위한 리스트
    for doc in print_list:
        prior_number.append(doc)

    # 큐 안에 index를 넣어 탐색
    result = [0 for _ in range(N)]
    queue = [i for i in range(N)]
    sequence = 1
    while queue:
        if print_list[queue[0]] == max(prior_number):
            prior_number.remove(max(prior_number))
            result[queue.pop(0)] = sequence
            sequence += 1
        else:
            queue.append(queue.pop(0))
    print(result[M])

# 1) prior_number에 모든 수를 넣어서 우선 순위 maximum 숫자를 확인할 때 쓴다. max(prior_number)

# 2) 큐 안에 N만큼의 index를 넣는다.

# 3) sequence로 해당 숫자가 몇 번째로 꺼내지는 지를 표시한다.

# 4-1-1) 큐의 맨 처음 index에 해당하는 printer_list의 숫자가 우선 순위가 가장 높다면 이를 result에 담는다.

# 4-1-2) prior_number에서 가장 큰 수를 하나 지워준다.

# 4-2)  else: 가장 높은 우선순위가 아니라면 큐 첫번째를 큐의 가장 뒷부분으로 다시 보낸다.

# 4-3) 반복한다.

# 내가 푼 방법은 좀 더 다양한 수가 나오면 틀리게 돼있는 것. 아예 배열을 새로 하나 파서 거기서 계속해서 제일 높은 수를 구해주면 됐는데. 그리고 sequence값을 0이아니라 1로 뒀어야 했다. 어차피 우선순위가 제일 빠르면 변동없이 1이니 디폴트 설정에도 신경써야 했다.
