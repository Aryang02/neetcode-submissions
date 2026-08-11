class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n//2):
            digits[i], digits[n-i-1] = digits[n-i-1], digits[i]
        
        print(digits)
        carry = 1
        for i in range(len(digits)):
            digits[i] = digits[i]+carry
            if digits[i]//10:
                carry = digits[i]//10
                digits[i] = digits[i]%10
            else:
                carry = 0
        if carry:
            digits.append(carry)
        return digits[::-1]