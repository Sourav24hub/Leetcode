class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        flag = True
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                flag = False
                break
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        if flag:
            return -1
        else:
            return mid