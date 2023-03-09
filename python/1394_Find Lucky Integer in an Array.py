from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)

        for val, occ in sorted(counter.items(), reverse=True):
            if val == occ:
                return val
        return -1
