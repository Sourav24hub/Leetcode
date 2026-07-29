class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        stack = []
        ans = {}
        for i in range(-1,-n-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = ans[nums1[i]]
        return nums1