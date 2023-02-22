class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}

        for i in range(len(s)):
            char = s[i]

            if char in dic:
                return char
            else:
                dic[char] = i
