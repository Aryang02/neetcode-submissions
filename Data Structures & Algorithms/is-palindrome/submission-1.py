class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                st+=s[i]
        print(st)
        return st.lower() == st[::-1].lower()