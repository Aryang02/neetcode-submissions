class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)

        res = []
        while i<n and intervals[i][1] < new[0]:
            res.append(intervals[i])
            i += 1
        
        while i<n and intervals[i][0] <= new[1]:
            new = [
                min(intervals[i][0], new[0]),
                max(intervals[i][1], new[1])
            ]
            i+= 1
        res.append(new)

        while i<n:
            res.append(intervals[i])
            i+=1
        
        return res