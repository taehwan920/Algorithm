from collections import defaultdict


def solution(K, travel):
    n = len(travel)
    dp = [defaultdict(int) for i in range(100)]
    dp[0][travel[0][0]] = travel[0][1] if travel[0][0] <= K else 0
    dp[0][travel[0][2]] = travel[0][3] if travel[0][2] <= K else 0
    MAX = 0
    for i in range(1, n):
        for time in dp[i-1]:
            time1, time2 = time + travel[i][0], time + travel[i][2]
            if time1 <= K:
                dp[i][time1] = max(dp[i][time1], dp[i-1][time] + travel[i][1])
                MAX = max(MAX, dp[i][time1])
            if time2 <= K:
                dp[i][time2] = max(dp[i][time2], dp[i-1][time] + travel[i][3])
                MAX = max(MAX, dp[i][time2])
    return MAX

# defaultdict(int) 는 문자열이 아닌 정수를 key로 지정할 수 있게 해주는 dict 모듈임.
# 각 연산을 dict에 저장함으로써 탐색 시간을 대폭 줄여서 시간복잡도를 줄인 케이스.
