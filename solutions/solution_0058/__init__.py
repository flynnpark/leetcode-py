class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])
