class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        result = 10 ** 10

        for i in range(len(position)):
            temp = 0
            for j in range(len(position)):
                temp += abs(position[i] - position[j]) % 2
            result = temp if temp < result else result

        return result
