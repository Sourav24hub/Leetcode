class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def merge(lis1,lis2):
            sortedLis = []
            i=j=0
            while i < len(lis1) and j < len(lis2):
                if lis1[i]<lis2[j]:
                    sortedLis.append(lis1[i])
                    i+=1
                else:
                    sortedLis.append(lis2[j])
                    j+=1
            sortedLis.extend(lis1[i:])
            sortedLis.extend(lis2[j:])
            return sortedLis
        sorted_nums = merge(nums1,nums2)
        mid = (len(sorted_nums))// 2
        if (len(sorted_nums)%2==0):
            median = ( sorted_nums[mid] + sorted_nums[(mid-1)] ) / 2.0
        else:
            median = sorted_nums[mid]
        return median