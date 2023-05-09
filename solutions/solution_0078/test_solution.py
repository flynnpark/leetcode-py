from typing import TypedDict

from . import Solution

CaseDict = TypedDict('CaseDict', {'input': list[int], 'expected': list[list[int]]})

test_cases: list[CaseDict] = [
    {
        'input': [1, 2, 3],
        'expected': [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
    },
    {
        'input': [],
        'expected': [[]],
    },
    {
        'input': [0],
        'expected': [[], [0]],
    },
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().subsets(test_case['input'])
        assert actual_result == test_case['expected']
