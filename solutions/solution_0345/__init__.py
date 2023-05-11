class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1

        temp = list(s)

        while left < right:
            if vowels.find(temp[left]) >= 0 and vowels.find(temp[right]) >= 0:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
            elif vowels.find(temp[left]) < 0:
                left += 1
            else:
                right -= 1

        return ''.join(temp)
