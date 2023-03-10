from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s).most_common()
        return "".join([str(val) * occ for val, occ in counter])
