from typing import Any, List
from solutions.solution_0049 import Solution

input_values = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
expected_outputs = [
    [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ],
    [[""]],
    [["a"]],
]


def sort_2d_list(list_item: List[List[Any]]) -> List[List[Any]]:
    result = []
    for item in list_item:
        result.append(sorted(item))
    return sorted(result)


def test_solution():
    for index, input_value in enumerate(input_values):
        actual_results = Solution().groupAnagrams(input_value)
        actual_results = sort_2d_list(actual_results)

        expected_results = sort_2d_list(expected_outputs[index])

        assert len(actual_results) == len(expected_results)
        assert actual_results == expected_results