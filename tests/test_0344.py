from solutions.solution_0344 import Solution


def test_solution():
    assert Solution().reverseString(s=["h", "e", "l", "l", "o"]) == [
        "o",
        "l",
        "l",
        "e",
        "h",
    ]
    assert Solution().reverseString(s=["H", "a", "n", "n", "a", "h"]) == [
        "h",
        "a",
        "n",
        "n",
        "a",
        "H",
    ]
    assert Solution().reverseString2(s=["h", "e", "l", "l", "o"]) == [
        "o",
        "l",
        "l",
        "e",
        "h",
    ]
    assert Solution().reverseString2(s=["H", "a", "n", "n", "a", "h"]) == [
        "h",
        "a",
        "n",
        "n",
        "a",
        "H",
    ]
