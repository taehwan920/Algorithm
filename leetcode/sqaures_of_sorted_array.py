class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        temp = list(map(lambda x: x * x, A))
        return sorted(temp)
