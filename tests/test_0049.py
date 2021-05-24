from solutions.solution_0049 import Solution


def test_solution():
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]