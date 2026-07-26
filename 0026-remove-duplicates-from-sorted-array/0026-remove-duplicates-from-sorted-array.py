class Solution(object):
    def removeDuplicates(self, nums):
        pntr = 0
        nxt = pntr + 1
        while nxt < len(nums):
            if nums[pntr] < nums[nxt]:
                nums[pntr+1] = nums[nxt]
                pntr += 1
            else:
                nxt += 1
        return pntr+1