class Solution(object):
    def findMin(self, nums):
        curr_min = nums[0]
        for i in nums:
            if i < curr_min:
                return i
        return curr_min