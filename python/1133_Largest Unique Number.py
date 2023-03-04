from collections import Counter

class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for num, occ in sorted(counter.items(), reverse=True):
            if occ == 1:
                return num
        return -1
