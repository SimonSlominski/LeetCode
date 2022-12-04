class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            stack.append(i)

            if len(stack) >= 2 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()

        return "".join(stack)
