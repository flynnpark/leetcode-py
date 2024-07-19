from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: str
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': 'bcabc',
        'expected': 'abc',
    },
    {'input': 'cbacdcbc', 'expected': 'acdb'},
]


def test_solution():
    for test_case in test_cases:
        result = Solution().removeDuplicateLetters(test_case['input'])
        assert result == test_case['expected']
