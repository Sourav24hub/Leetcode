class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        l1 = [-1,-1]
        change = 0
        while left < len(nums):
            if nums[left] == target:
                l1[0] = left
                change += 1
                break
            left += 1
        while right > -1:
            if nums[right] == target:
                l1[1] = right
                change += 1
                break
            right -= 1
        if change == 2:
            return l1
        else:
            return [-1,-1]