class Solution(object):
    def sortColors(self, nums):
        front,pntr = 0,0
        back = len(nums)-1
        while pntr<=back:
            if nums[pntr] == 0:
                nums[pntr],nums[front] = nums[front],nums[pntr]
                pntr += 1
                front += 1
            elif nums[pntr] == 1:
                pntr += 1
            else:
                nums[pntr],nums[back] = nums[back],nums[pntr]
                back -= 1
        return nums