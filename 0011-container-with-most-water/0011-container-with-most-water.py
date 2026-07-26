class Solution(object):
    def maxArea(self, height):
        left,right = 0,(len(height)-1)
        water = 0
        while left < right:
            hight = min(height[left], height[right])
            width = (right - left)
            volume = hight*width
            water = max(water,volume)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return water