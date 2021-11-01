from solutions.solution_0641 import MyCircularDeque


def test_solution():
    myCircularDeque = MyCircularDeque(3)
    assert myCircularDeque.insertLast(1) is True
    assert myCircularDeque.insertLast(2) is True
    assert myCircularDeque.insertFront(3) is True
    assert myCircularDeque.insertFront(4) is False
    assert myCircularDeque.getRear() == 2
    assert myCircularDeque.isFull() is True
    assert myCircularDeque.deleteLast() is True
    assert myCircularDeque.insertFront(4) is True
    assert myCircularDeque.getFront() == 4
