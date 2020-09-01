class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        could = False
        while bills:
            payment = bills.pop(0)
            if payment == 5:
                fives += 5
            else:
                change = payment - 5
                if change == 5:
                    tens += 10
                    fives -= 5
                    if fives < 0:
                        could = False
                        break
                elif change == 15:
                    if fives:
                        if tens:
                            tens -= 10
                            fives -= 5
                        else:
                            fives -= 15
                        if tens < 0 or fives < 0:
                            could = False
                            break
                    else:
                        could = False
                        break
                could = True
        return could
