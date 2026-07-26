class Solution(object):
    def findMaxLength(self, nums):
        dic = {0:-1}
        sums = 0
        curr_lnth = 0
        max_lnth = 0
        for i in range(0,len(nums)):
            if  nums[i] == 0:
                sums -= 1
            else:
                sums += 1
            if sums in dic:
                curr_lnth = i - dic[sums]
                max_lnth = max(curr_lnth, max_lnth)
            else:
                dic[sums] = i
        return max_lnth