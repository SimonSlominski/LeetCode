class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return all(num[i] + num[~i] in "696 00 88 11" for i in range(len(num) // 2 + 1))
