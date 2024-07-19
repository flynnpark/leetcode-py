import sys


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_average = -sys.maxsize
        for i in range(0, len(nums) - k + 1):
            max_average = max(max_average, sum(nums[i : i + k]) / k)
        return max_average
