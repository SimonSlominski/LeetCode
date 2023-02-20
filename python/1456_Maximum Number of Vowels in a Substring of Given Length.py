class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"

        out = 0
        for right in range(k):
            if s[right] in vowels:
                out += 1

        curr = out
        for right in range(k, len(s)):
            if s[right] in vowels:
                curr += 1
            if s[right - k] in vowels:
                curr -= 1
            out = max(out, curr)
        return out
