class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        first_unique = 0
        longest_subs = 0
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= first_unique:
                first_unique = map[s[i]] + 1
            map[s[i]] = i
            longest_subs = max(longest_subs, i - first_unique + 1)
        return longest_subs