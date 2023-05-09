from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: list[list[str]]
    expected: list[str]


test_cases: list[CaseDict] = [
    {
        'input': [
            ['MUC', 'LHR'],
            ['JFK', 'MUC'],
            ['SFO', 'SJC'],
            ['LHR', 'SFO'],
        ],
        'expected': ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
    },
    {
        'input': [
            ['JFK', 'SFO'],
            ['JFK', 'ATL'],
            ['SFO', 'ATL'],
            ['ATL', 'JFK'],
            ['ATL', 'SFO'],
        ],
        'expected': ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().findItinerary(test_case['input'])
        expected = test_case['expected']
        assert actual == expected
