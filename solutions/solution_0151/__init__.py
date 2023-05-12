class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([item for item in s.strip().split(' ') if item]))
