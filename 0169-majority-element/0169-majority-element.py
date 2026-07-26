class Solution(object):
    def majorityElement(self, nums):
        di = {}
        for item in nums:
            if item not in di:
                di[item] = nums.count(item)
        res,counter = 0,0
        for key in di:
            res = key if di[key] > counter else res
            counter = max(counter,di[key])
        return res