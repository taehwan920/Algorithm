class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens:
            return 0

        tokens.sort()

        point = 0
        while tokens:
            if P < tokens[0]:
                if point and len(tokens) > 1:
                    P += tokens.pop()
                    point -= 1
                else:
                    break
            else:
                P -= tokens.pop(0)
                point += 1

        return point

# 그리디 알고리즘
# 처음에 주어진건 tokens와 P(Power).
# 이 두 재화를 활용하여 가장 높은 점수를 획득하는 게 목적.
# 가장 싼 token[i]를 사서 point를 획득하고, 가장 비싼 token[i]를 point를 소비해 P를 획득해야 가장 많은 점수를 획득할 수 있다.
# 맨 처음엔 가장 싼 token을 P를 사용해 구매하여 point를 획득한다. P가 token[0]보다 크거나 같으면 계속 구매하여 point획득.
# 만약 P가 token[0]보다 작은데 point가 0이라면 거기서 끝. point가 0이 아니라면 point를 소비하여 P를 다시 늘리는데, 이때는 가장 비싼 token인 token[-1]을 point로 구매.
# 하지만 token을 point로 구매하기 전에 남은 token이 1 혹은 0이라면 point를 소비해서 token을 사봐야 아무 의미가 없으므로 사지 않고 반복문 종료.
