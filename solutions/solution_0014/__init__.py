class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = []
        for pair in zip(*strs, strict=False):
            pair_set = set(pair)
            if len(pair_set) == 1:
                result.append(pair_set.pop())
            else:
                break
        return ''.join(result)
