class Solution(object):
    def backspaceCompare(self, s, t):
        def stack(st):
            stck = []
            for i in st:
                if i == "#":
                    if stck:
                        stck.pop()
                else:
                    stck.append(i)
            return stck
        return stack(s) == stack(t)