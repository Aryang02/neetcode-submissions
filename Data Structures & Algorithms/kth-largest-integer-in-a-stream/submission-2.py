class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.maxh = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if not self.maxh or len(self.maxh) < self.k:
            self.maxh.append(val) 
        if val > self.maxh[-1]:
            self.maxh.pop()
            self.maxh.append(val)
        self.maxh = sorted(self.maxh,reverse=True)
        return self.maxh[self.k-1]
