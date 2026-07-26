class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=""
        flag = True
        minm = min(strs, key=len)
        for i in range(len(minm)):
            for item in strs:
                if minm[i] != item[i]:
                    flag = False
            if flag == True:
                prefix += minm[i]
        return prefix