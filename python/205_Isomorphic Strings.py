class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            if t[i] not in t_dict:
                t_dict[t[i]] = s[i]
            if s_dict[s[i]] != t[i] or t_dict[t[i]] != s[i]:
                return False

        return True
