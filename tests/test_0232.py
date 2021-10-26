from solutions.solution_0232 import MyQueue


def test_solution():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False
