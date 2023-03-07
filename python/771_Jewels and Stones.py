class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        out = 0
        for char in jewels:
            if char in stones:
                out += stones.count(char)
        return out
