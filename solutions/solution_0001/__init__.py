class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            rest = target - num
            # target에서 num을 뺀 숫자가 해시 테이블에 존재할 경우
            if rest in dict_nums:
                return [dict_nums[rest], index]
            # 그 외의 경우
            else:
                dict_nums[num] = index
        return []
