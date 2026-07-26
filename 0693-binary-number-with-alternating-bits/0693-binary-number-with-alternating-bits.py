class Solution(object):
    def hasAlternatingBits(self, n):
        bnry = bin(n)
        relevant = bnry[2:]
        for i in range(0,len(relevant)-1):
            if relevant[i] == relevant[(i+1)]:
                return False
        return True