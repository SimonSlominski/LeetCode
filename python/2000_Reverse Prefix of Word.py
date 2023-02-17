class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word

        out = ""

        for i, char in enumerate(word):
            if char == ch:
                out += word[:i + 1][::-1] + word[i + 1:]
                break

        return out
