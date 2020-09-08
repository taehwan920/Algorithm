def sum_digits(n):
    s = list(str(n))
    n = list(map(int, s))
    return sum(n)


class Solution:
    def countLargestGroup(self, n: int) -> int:
        board = [0 for i in range(40)]

        for i in range(1, n+1):
            if i < 10:
                board[i] += 1
                continue
            temp = sum_digits(i)
            board[temp] += 1

        biggest = max(board)

        return board.count(biggest)
