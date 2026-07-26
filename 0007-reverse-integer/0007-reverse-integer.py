class Solution(object):
    def reverse(self, x):
        def rev(x):
            rvr = 0
            while x != 0:
                rem = x%10
                x //= 10
                rvr = rvr*10 + rem
            return rvr
        if x > 0:
            rvrse = rev(x)
        elif x < 0:
            x = abs(x)
            rvrse = 0 - rev(x)
        else:
            return 0
        if rvrse > -2**31 and rvrse < 2**31:
            return rvrse
        else:
            return 0