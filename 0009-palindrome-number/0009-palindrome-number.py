class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            strng = str(x)
            if strng == strng[::-1]:
                return True
            else:
                return False