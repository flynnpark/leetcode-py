from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    s: str
    words: list[str]


class CaseDict(TypedDict):
    input: InputDict
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            's': 'barfoothefoobarman',
            'words': ['foo', 'bar'],
        },
        'expected': [0, 9],
    },
    {
        'input': {
            's': 'wordgoodgoodgoodbestword',
            'words': ['word', 'good', 'best', 'word'],
        },
        'expected': [],
    },
    {
        'input': {
            's': 'barfoofoobarthefoobarman',
            'words': ['bar', 'foo', 'the'],
        },
        'expected': [6, 9, 12],
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().findSubstring(**test_case['input'])
    assert result == test_case['expected']
