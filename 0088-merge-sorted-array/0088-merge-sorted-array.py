class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        while m < len(nums1):
            nums1[m],nums2[i] = nums2[i],nums1[m]
            m += 1
            i += 1
        nums1.sort()    