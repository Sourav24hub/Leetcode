class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = -1
        length = 0
        while i >= -len(s) and s[i] != " ":
            length += 1
            i -= 1
        return length