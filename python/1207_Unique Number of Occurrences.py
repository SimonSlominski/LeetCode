from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = Counter(arr)
        return sum(set(counter.values())) == sum(counter.values())
