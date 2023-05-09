from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    numCourses: int
    prerequisites: list[list[int]]


class CaseDict(TypedDict):
    input: InputDict
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': {
            'numCourses': 2,
            'prerequisites': [[1, 0]],
        },
        'expected': True,
    },
    {
        'input': {
            'numCourses': 2,
            'prerequisites': [[1, 0], [0, 1]],
        },
        'expected': False,
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().canFinish(**test_case['input'])
        expected = test_case['expected']
        assert actual == expected
