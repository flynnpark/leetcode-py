import collections
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        freq = collections.Counter(nums)

        for num in nums:
            if num in freq and freq[num] > 0:
                freq[num] -= 1
                diff = k - num
                if diff in freq and freq[diff] > 0:
                    freq[diff] -= 1
                    result += 1
                else:
                    freq[num] += 1

        return result
