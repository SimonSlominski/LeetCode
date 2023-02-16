class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha_str = "".join([char for char in s if char.isalpha()])
        right = len(alpha_str) -1

        out = ""

        for left in s:
            if left.isalpha():
                out += alpha_str[right]
                right -= 1
            else:
                out += left

        return out
