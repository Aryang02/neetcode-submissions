class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''
        for x in s:
            if x.isalpha() or x.isdigit():
                strs+= x.lower()
        return (strs == strs[::-1])

        