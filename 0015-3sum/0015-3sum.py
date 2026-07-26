class Solution(object):
    def threeSum(self, nums):
        ans = []
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target= -nums[i]
            left=i+1
            right=n-1
            while left<right:
                two_sum=nums[left]+nums[right]
                if two_sum==target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1    
                elif two_sum<target:
                    left+=1
                else:
                    right-= 1
        return ans