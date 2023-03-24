class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        result = ""
        for c in order:
            if c in count:
                result += c * count[c]
                del count[c]

        for c in count:
            result += c * count[c]

        return result
