class Solution(object):
    def isPalindrome(self, head):
        curr = head
        lis = []
        while curr:
            lis.append(curr.val)
            curr = curr.next
        rev = lis[::-1]
        return rev == lis