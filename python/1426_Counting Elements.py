class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return sum(1 for x in arr if x + 1 in arr)
