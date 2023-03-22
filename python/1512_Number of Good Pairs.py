class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        dict_number = dict()
        for n in nums:
            if n in dict_number:
                output += dict_number[n]
                dict_number[n] += 1
            else:
                dict_number[n] = 1
        return output
