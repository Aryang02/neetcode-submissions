class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)            
            x = n
            digits = []
            while True:
                r = x%10
                x = x//10
                digits.append(r**2)
                if not x:
                    break
            if x and x<10:
                digits.append(r**2)
            n = sum(digits)

        return True