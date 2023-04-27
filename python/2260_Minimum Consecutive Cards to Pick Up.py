from collections import defaultdict

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)

        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)

        return ans if ans < float("inf") else -1
