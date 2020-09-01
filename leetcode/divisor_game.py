class Solution:
    def divisorGame(self, N: int) -> bool:
        moved = True
        alice = True
        while moved:
            moved = False
            nums = [i for i in range(1, N)]
            sanitized = list(filter(lambda x: N % x == 0, nums))
            if sanitized:
                moved = True
                alice = not alice
                N = N - sanitized[0]
            else:
                break

        if alice:
            return False
        else:
            return True
