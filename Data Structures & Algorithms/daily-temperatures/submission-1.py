class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [len(temps)-1]
        res = [0]
        for i in range(len(temps)-2, -1, -1):
            while stack and temps[stack[-1]]<=temps[i]:
                stack.pop()
            if stack:
                res.append(stack[-1]-i)
            else:
                res.append(0)
            stack.append(i)
        
        for i in range(len(temps)//2):
            res[i], res[len(temps)-i-1] = res[len(temps)-i-1], res[i]
        
        return res