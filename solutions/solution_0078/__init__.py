class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index: int, path: list[int]):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        result = []
        dfs(0, [])
        return result
