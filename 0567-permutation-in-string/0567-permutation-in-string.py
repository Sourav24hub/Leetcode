from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        i = 0
        j = len(s1) - 1
        seen = Counter(s2[0:j+1])
        compare = Counter(s1)
        while j < len(s2) - 1 and seen != compare:
            seen[s2[i]] -= 1
            if seen[s2[i]] == 0:
                del seen[s2[i]]
            i += 1
            j += 1
            seen[s2[j]] += 1
        if seen == compare:
            return True
        else:
            return False