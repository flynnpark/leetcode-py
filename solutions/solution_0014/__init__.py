from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for pair in zip(*strs):
            pair_set = set(pair)
            if len(pair_set) == 1:
                result.append(pair_set.pop())
            else:
                break
        return "".join(result)
