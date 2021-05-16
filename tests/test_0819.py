from solutions.solution_0819 import Solution

TEST_INPUT = [
    {
        "paragraph": "Bob hit a ball, the hit BALL flew far after it was hit.",
        "banned": ["hit"],
    },
    {"paragraph": "a.", "banned": []},
]

TEST_OUTPUT = ["ball", "a"]


def test_solution():
    for index, input in enumerate(TEST_INPUT):
        assert (
            Solution().mostCommonWord(
                paragraph=input["paragraph"], banned=input["banned"]
            )
            == TEST_OUTPUT[index]
        )
