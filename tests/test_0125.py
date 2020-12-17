from solutions.solution_0125 import Solution, Solution2, Solution3


examples = ["A man, a plan, a canal: Panama", "race a car"]


def test_solution():
    assert Solution().isPalindrome(examples[0]) == True
    assert Solution().isPalindrome(examples[1]) == False
    assert Solution2().isPalindrome(examples[0]) == True
    assert Solution2().isPalindrome(examples[1]) == False
    assert Solution3().isPalindrome(examples[0]) == True
    assert Solution3().isPalindrome(examples[1]) == False
