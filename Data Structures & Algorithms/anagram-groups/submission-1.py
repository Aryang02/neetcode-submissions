class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        for s in strs:
            if ''.join(sorted(s)) in map1.keys():
                map1[''.join(sorted(s))].append(s)
            else:
                map1[''.join(sorted(s))] = [s]
        res = []
        for v in map1.values():
            res.append(v)
        return res
