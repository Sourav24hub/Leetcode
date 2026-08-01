class Solution(object):
    def isPalindrome(self, head):
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        return lis == lis[::-1]