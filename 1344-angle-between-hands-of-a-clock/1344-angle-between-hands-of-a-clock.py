from math import fabs
class Solution(object):
    def angleClock(self, hour, minutes):
        hr_angle = hour*30+minutes*0.5
        min_angle = minutes*6
        angle = fabs(hr_angle-min_angle)
        if angle > 360 - angle:
            return 360 - angle
        return angle