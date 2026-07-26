class Solution(object):
    def subarraysDivByK(self, nums, k):
        sum,res = 0,0
        d = {0:1}
        for item in nums:
            sum+=item
            rem = sum%k
            if rem in d:
                res += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
        return res