class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        concat_words = [""]
        for substring in filter(lambda x: len(x) == len(set(x)), arr):
            concat_words += [char + substring for char in concat_words if not set(char) & set(substring)]
        return max(map(len, concat_words))
