class Solution(object):
    def maxSubArray(self, nums):

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = 1
        max_sum = curr_sum = nums[0]

        while right < len(nums):

            curr_sum = max(nums[right],curr_sum+nums[right])
            max_sum = max(curr_sum,max_sum)
            right += 1
        
        return max_sum