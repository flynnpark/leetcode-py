import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = sys.maxsize
        second = sys.maxsize

        for num in nums:
            if num > second:
                return True

            if num > first:
                second = min(num, second)

            else:
                first = min(num, first)

        return False
