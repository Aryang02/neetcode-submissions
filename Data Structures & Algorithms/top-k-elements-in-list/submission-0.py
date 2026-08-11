class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        res_dic = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))
        res = []
        for i in range(k):
            res.append(list(res_dic.keys())[i])
        return res