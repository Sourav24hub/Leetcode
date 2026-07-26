class Solution(object):
    def containsDuplicate(self, nums):
        di={}
        for i in nums:
            if i in di:
                return True
            di[i] = 0
        return False