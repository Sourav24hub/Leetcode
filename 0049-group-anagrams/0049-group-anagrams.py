from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        finall = []
        grouped = defaultdict(list)
        for item in strs:
            sorted_item = tuple(sorted(item))
            grouped[sorted_item].append(item)
        for keys in grouped:
            finall.append(grouped[keys])
        return finall