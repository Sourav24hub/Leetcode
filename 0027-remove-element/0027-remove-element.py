class Solution(object):
    def removeElement(self, nums, val):
        b = 0
        e = len(nums) - 1
        while e>=b:
            if nums[b] == val and nums[e] != val:
                nums[b],nums[e] = nums[e],nums[b]
                e -= 1
                b += 1
            elif nums[b] == val and nums[e] == val:
                e -= 1
            else:
                b += 1
        return len(nums) - nums.count(val)