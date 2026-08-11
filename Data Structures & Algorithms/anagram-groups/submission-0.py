class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        
        for s in strs:
            if (''.join(sorted(s))) not in dic:
                dic[''.join(sorted(s))] = [s]
            else:
                dic[''.join(sorted(s))].append(s) 
        for x in dic:
            res.append(dic[x])
        return res
            
