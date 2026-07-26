class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        for index, value in enumerate(nums):
            comp = target - value
            if comp in dict1:
                lit = []
                lit.extend([dict1[comp],index])
                break
            else:
                dict1[value]=index
                continue
        return lit