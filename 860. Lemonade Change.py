class Solution(object):
    def lemonadeChange(self, bills):
        five, ten = 0, 0

        for i in range(0, len(bills)):

            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False

            else:
                if (five and ten):
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True