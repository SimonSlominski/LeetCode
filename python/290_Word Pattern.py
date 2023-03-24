class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(pattern) != len(s.split()):
            return False

        map_dict = {}

        for i in range(len(pattern)):
            if pattern[i] not in map_dict:
                map_dict[pattern[i]] = s.split()[i]
            if map_dict[pattern[i]] != s.split()[i] or len(set(map_dict.values())) != len(map_dict.values()):
                return False

        return True
