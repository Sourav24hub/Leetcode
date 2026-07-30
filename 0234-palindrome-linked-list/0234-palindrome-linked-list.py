class Solution(object):
    def isPalindrome(self, head):
        curr = head
        lis = []
        while curr:
            lis.append(curr.val)
            curr = curr.next
        left = 0
        right = len(lis) - 1
        while left <= right:
            if lis[left] != lis[right]:
                return False
            left += 1
            right -= 1
        return True