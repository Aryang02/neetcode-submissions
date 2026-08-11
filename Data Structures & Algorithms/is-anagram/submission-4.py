class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        i = 0
        while i < len(s):
            if s[i] in map1.keys():
                map1[s[i]] += 1
            else:
                map1.update({s[i]: 1})
            if t[i] in map2.keys():
                map2[t[i]] += 1
            else:
                map2.update({t[i]: 1})
            i += 1 
        return map1 == map2   
        