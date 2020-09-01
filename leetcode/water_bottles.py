class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        rest = 0
        while numBottles:
            drink += numBottles
            entire = numBottles + rest
            numBottles = entire // numExchange
            rest = entire % numExchange

        return drink
