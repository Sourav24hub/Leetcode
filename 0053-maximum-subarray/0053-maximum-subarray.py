class Solution(object):
    def maxSubArray(self, nums):
        
        pntr = 1
        max_sum = curr_sum = nums[0]

        while pntr < len(nums):

            curr_sum = max(nums[pntr],curr_sum+nums[pntr])
            max_sum = max(curr_sum,max_sum)
            pntr += 1
        
        return max_sum