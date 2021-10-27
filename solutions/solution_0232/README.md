## 0232. [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

`- void push(int x)` Pushes element x to the back of the queue.

- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

##### **Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

#### **Example 1:**

<pre><code><strong>Input</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</code></pre>

#### **Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

## 해결 방법

이번에는 스택(Stack)을 사용하여 큐(Queue)를 구현하는 문제이다. 제한사항 역시 스택의 기본 연산만을 사용하여 구현해야 한다. 이전에 큐를 사용하여 스택을 구현하는 것과 같은 방법으로 구현할 수 있을까 싶었는데, 하나의 스택을 이용해서 해결할 수 없어 2개의 스택을 이용해야 한다.

2개의 스택은 `input`, `output`으로 명명하고, `input` 스택은 `push`에서 값을 입력할 때 사용하고, `output`은 `pop`과 `peek`에서 사용한다. `pop`과 `peek`는 같은 데이터를 보여주지만 `pop`은 데이터를 제거하고 `peek`은 그냥 보여주기만 하므로, `peek`에서 `input` 스택을 사용하여 `output` 스택을 역순으로 만들어 주는 부분을 추가한다. 이 때, `output`이 비어있을 때만 `input`을 사용하여 `output`을 채우는 것이 좋다. 이렇게 하면 `output`이 모두 `pop`되기 전까지는 다시 `output`에 입력이 일어나지 않으므로 시간복잡도는 O(1)이 된다.
