class Solution(object):
    def nextGreaterElements(self, nums):
        stack = nums[::-1]
        n = len(nums)
        ans = [0]*n
        for i in range (n-1,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans