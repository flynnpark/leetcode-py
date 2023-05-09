class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        result = []

        for i in range(max_length):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        return ''.join(result)
