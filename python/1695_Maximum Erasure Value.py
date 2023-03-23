class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        left, mx, ans = 0, 0, 0

        for idx, num in enumerate(nums):
            if num in seen:
                while left < seen[num] + 1:
                    mx -= nums[left]
                    left += 1
            seen[num] = idx
            mx += num
            ans = max(ans, mx)

        return ans
