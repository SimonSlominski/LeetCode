import itertools


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder = {0: -1} # map remainder -> end index
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False

        # This solution was too slow
        # i = 0
        # list_of_num = []
        # while i < len(nums)-1:
        #     for num in nums[i:]:
        #         list_of_num.append(num)
        #         if sum(list_of_num) % k == 0 and len(list_of_num) >= 2:
        #             return True
        #     i += 1
        #     list_of_num = []
        # return False
