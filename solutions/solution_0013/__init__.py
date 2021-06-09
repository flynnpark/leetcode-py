ROMAN_DICT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if i > 0 and ROMAN_DICT[s[i]] > ROMAN_DICT[s[i - 1]]:
                result += ROMAN_DICT[s[i]] - (ROMAN_DICT[s[i - 1]] * 2)
            else:
                result += ROMAN_DICT[s[i]]
        return result
