class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        origin = [i[0] for i in paths]
        dest = [i[1] for i in paths]

        for city in dest:
            if city not in origin:
                return city
