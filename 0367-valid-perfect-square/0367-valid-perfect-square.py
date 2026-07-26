import math
class Solution(object):
    def isPerfectSquare(self, num):
        root = num**0.5
        if (math.modf(root))[0] == 0.0:
            return True
        else:
            return False