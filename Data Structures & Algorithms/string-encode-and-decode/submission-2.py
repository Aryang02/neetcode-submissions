class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        combined = ""
        for s in strs:
            combined = combined + "?-?" + s
        return combined

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split("?-?")[1:]