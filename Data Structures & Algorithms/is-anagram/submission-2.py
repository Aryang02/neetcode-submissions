class Solution:

    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for x in s:
            if dic[x]:
                dic[x] += 1
            else:
                dic[x] = 1
        for x in t:
            if dic[x]:
                dic[x] -= 1
            else:
                return False
        if max(dic.values()) == 0:
            return True
        return False

