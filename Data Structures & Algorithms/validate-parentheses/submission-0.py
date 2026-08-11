class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{',']':'['}
        stack = []

        for x in s:
            if x not in dic:
                stack.append(x)
                continue
            if not stack or stack[-1] != dic[x]:
                return False
            stack.pop()
        
        return not stack
