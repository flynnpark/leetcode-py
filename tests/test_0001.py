from solutions.solution_0001 import Solution


def test_solution():
    assert Solution().twoSum(nums=[2,7,11,15], target=9) == [0, 1]
    assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1]
