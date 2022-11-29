class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                print(i, dic[num])
                return True
            dic[num] = i
        return False
