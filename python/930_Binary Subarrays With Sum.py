from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        dic = defaultdict(int)
        dic[0] = 1
        ans = curr = 0
        for num in nums:
            curr += num
            ans += dic[curr - goal]
            dic[curr] += 1
        return ans
