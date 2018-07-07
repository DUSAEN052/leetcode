from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bank = 0
        ddict = defaultdict(int)

        for bill in bills:
            change = bill - 5
            bank += bill

            if change > bank:
                return False

            ddict[bill] += 1

            while change != 0:
                if change >= 20 and ddict[20] > 0:
                    change -= 20
                    bank -= 20
                    ddict[20] -= 1
                elif change >= 10 and ddict[10] > 0:
                    change -= 10
                    bank -= 10
                    ddict[10] -= 1
                elif change >= 5 and ddict[5] > 0:
                    change -= 5
                    bank -= 5
                    ddict[5] -= 1
                else:
                    return False

            if change > 0:
                return False

        return True
