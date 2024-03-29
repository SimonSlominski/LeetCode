class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = set()
        x = y = 0
        for di in path:
            visited.add((x, y))
            if di == "N":
                y += 1
            elif di == "S":
                y -= 1
            elif di == "E":
                x += 1
            elif di == "W":
                x -= 1
            if (x, y) in visited:
                return True
        return False
