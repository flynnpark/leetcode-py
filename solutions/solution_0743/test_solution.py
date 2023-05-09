from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    times: list[list[int]]
    n: int
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'times': [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
            'n': 4,
            'k': 2,
        },
        'expected': 2,
    },
    {
        'input': {
            'times': [[1, 2, 1]],
            'n': 2,
            'k': 1,
        },
        'expected': 1,
    },
    {
        'input': {
            'times': [[1, 2, 1]],
            'n': 2,
            'k': 2,
        },
        'expected': -1,
    },
    {
        'input': {
            'times': [
                [3, 1, 5],
                [3, 2, 2],
                [2, 1, 2],
                [3, 4, 1],
                [4, 5, 1],
                [5, 6, 1],
                [6, 7, 1],
                [7, 8, 1],
                [8, 1, 1],
            ],
            'n': 8,
            'k': 3,
        },
        'expected': 5,
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().networkDelayTime(**test_case['input'])
        expected = test_case['expected']
        assert actual == expected
