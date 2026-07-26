class Solution(object):
    def moveZeroes(self, nums):
        pntr = 0
        nxt = pntr + 1
        while nxt < len(nums):
            if nums[pntr] == 0:
                if nums[nxt] != 0:
                    nums[pntr],nums[nxt] = nums[nxt],nums[pntr]
                else:
                    nxt += 1
            else:
                pntr += 1
                nxt += 1
        return nums