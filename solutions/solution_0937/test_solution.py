from . import Solution

TEST_INPUT_LOGS = [
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
    ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
]

TEST_OUTPUT_LOGS = [
    ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
    ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
]


def test_solution():
    for index, input in enumerate(TEST_INPUT_LOGS):
        assert Solution().reorderLogFiles(input) == TEST_OUTPUT_LOGS[index]
