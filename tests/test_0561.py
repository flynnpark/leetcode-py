from typing import TypedDict

from solutions.solution_0561 import Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [1, 4, 3, 2],
        'expected': 4,
    },
    {
        'input': [6, 2, 6, 5, 1, 2],
        'expected': 9,
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().arrayPairSum(test_case['input'])
        expected = test_case['expected']
        assert actual == expected
