from solutions.solution_0002 import Solution


def test_solution():
    assert Solution().addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]) == [7, 0, 8]
    assert Solution().addTwoNumbers(l1=[0], l2=[0]) == [0]
    assert Solution().addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]
