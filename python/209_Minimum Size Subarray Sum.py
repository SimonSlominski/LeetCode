class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0

        left = total = 0
        out = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                out = min(out, right - left + 1)
                total -= nums[left]
                left += 1

        return out
