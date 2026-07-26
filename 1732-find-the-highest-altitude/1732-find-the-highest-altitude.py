class Solution(object):
    def largestAltitude(self, gain):
        curr_max = 0
        point = 0
        for item in gain:
            point += item
            curr_max = max(point, curr_max)
        return curr_max