class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=right=window = 0
        seen = set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            window = max(window,right-left)
        return window