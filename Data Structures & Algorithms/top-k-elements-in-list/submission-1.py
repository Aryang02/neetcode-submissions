class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = defaultdict(int)
        for num in nums:
            map1[num] += 1
        map1 = dict(sorted(map1.items(), key = lambda x: x[1], reverse=True))
        
        res = []
        for i in range(k):
            res.append(list(map1.keys())[i])

        return res