class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(rest_target: int, index: int, path: list[int]):
            if rest_target == 0:
                result.append(path)
                return
            if rest_target < 0:
                return

            for i in range(index, len(candidates)):
                dfs(rest_target - candidates[i], i, path + [candidates[i]])

        result = []
        dfs(target, 0, [])
        return result
