from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        occurs_twice = [num for num, cnt in Counter(nums).most_common(1)]
        missing_element = list(set(range(1, len(nums)+1)) - set(nums))

        return occurs_twice + missing_element
