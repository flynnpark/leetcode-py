class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []

        temp = 1
        for i in range(0, len(nums)):
            result.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result
