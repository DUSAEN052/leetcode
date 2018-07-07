class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stcks, stckt = [], []

        for s in S:
            if s is not '#':
                stcks.append(s)
            elif s == '#' and stcks:
                stcks.pop()

        for t in T:
            if t is not '#':
                stckt.append(t)
            elif t == '#' and stckt:
                stckt.pop()

        return stcks == stckt
