## 0225. [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the MyStack class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

##### **Notes:**

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

#### **Example 1:**

<pre><code><strong>Input</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 2, 2, false]

<strong>Explanation</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
</code></pre>

#### **Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

## 해결 방법

큐(Queue)를 사용하여 스택(Stack)을 구현하는 문제이다. 제한 사항은. 하나는 큐에서 사용하는 기본적인 연산만 사용해야 한다는 것이다. 큐는 FIFO이므로 FILO가 가능하도록 해주어야 하는데, 때문에 `push` 구현시에 새 아이템을 넣고 나머지 아이템들을 다시 너헝주는 방식으로 쉽게 구현할 수 있다. 나머지는 어렵지 않으므로 설명은 패스.
