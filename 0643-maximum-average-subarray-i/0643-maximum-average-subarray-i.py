class Solution(object):  
    def findMaxAverage(self, nums, k):
        i = 0
        j = k
        sum1 = sum(nums[i:j])
        new_sum = sum1
        while j < len(nums):
            new_sum += nums[j] - nums[i]
            sum1 = max(new_sum,sum1)
            j += 1
            i += 1
        return sum1/float(k)