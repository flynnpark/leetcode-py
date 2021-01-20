from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            rest = target - num
            if rest in dict_nums:
                return [dict_nums[rest], index]
            else:
                dict_nums[num] = index
