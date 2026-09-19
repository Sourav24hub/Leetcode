import math
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        i = 0
        closest_sum = nums[i] + nums[i+1] + nums[n-1]
        while i < n-1:
            left = i+1
            right = n-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if math.fabs(target-curr_sum) < math.fabs(target-closest_sum):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum
            i += 1
        return closest_sum