class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        curr_sum = 0
        d={0:1}
        for i in range(0,len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in d:
                count += d[curr_sum-k]
            d[curr_sum] = d.get(curr_sum,0) + 1
        return count