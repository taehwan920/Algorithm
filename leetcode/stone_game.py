class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a, l = 0, 0

        turn = 0
        while piles:
            if len(piles) == 1:
                l += piles.pop()
            else:
                if piles[0] > piles[-1]:
                    if turn % 2 == 0:
                        a += piles.pop(0)
                    else:
                        l += piles.pop()
                else:
                    if turn % 2 == 0:
                        a += piles.pop()
                    else:
                        l += piles.pop(0)
            turn += 1

        return True if a > l else False

# 그냥 문제 그대로 구현함.
