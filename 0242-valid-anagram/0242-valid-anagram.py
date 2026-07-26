class Solution(object):
    def isAnagram(self, s, t):
        def frequency(word):
            word = word.lower()
            d1={}
            for i in range(0,len(word)):
                if word[i] not in d1:
                    d1[word[i]] = word.count(word[i])
            return d1
        dict_s = frequency(s)
        dict_t = frequency(t)
        if dict_s == dict_t:
            return bool(1)
        return bool(0)