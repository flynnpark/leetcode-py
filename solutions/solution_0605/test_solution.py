from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    flowerbed: list[int]
    n: int


class CaseDict(TypedDict):
    input: InputDict
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': {
            'flowerbed': [1, 0, 0, 0, 1],
            'n': 1,
        },
        'expected': True,
    },
    {
        'input': {
            'flowerbed': [1, 0, 0, 0, 1],
            'n': 2,
        },
        'expected': False,
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().canPlaceFlowers(**test_case['input'])
        assert result == test_case['expected']
