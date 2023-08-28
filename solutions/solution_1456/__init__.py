import sys


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_vowels_length = 0
        current_substr_length = 0

        for left in range(len(s)):
            if s[left] in vowels:
                current_substr_length += 1

            if left >= k and s[left - k] in vowels:
                current_substr_length -= 1

            max_vowels_length = max(max_vowels_length, current_substr_length)

        return max_vowels_length
