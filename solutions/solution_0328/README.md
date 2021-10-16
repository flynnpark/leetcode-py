## 0328. [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

#### **Example 1:**

![](../../images/oddeven-linked-list.jpg)

<pre><code><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,3,5,2,4]</code></pre>

#### **Example 2:**

![](../../images/oddeven2-linked-list.jpg)

<pre><code><strong>Input:</strong> head = [2,1,3,5,6,4,7]
<strong>Output:</strong> [2,3,6,7,1,5,4]</code></pre>

#### **Constraints:**

- `n == number` of nodes in the linked list
- `0 <= n <= 10<sup>4</sup>`
- `-10<sup>6</sup> <= Node.val <= 10<sup>6</sup>`

## 해결 방법

주어진 링크드리스트를 홀수 번째 숫자와 짝수 번째 숫자로 묶은 뒤, 홀수 번째 숫자로 이루어진 노드 뒤에 짝수 번째 숫자로 이루어진 노드로 정렬해서 출력해야 하는 문제이다. 추가적인 요구사항으로는 `O(1)` 공간 복잡도와 `O(n)` 시간 복잡도에 풀이해야 한다.

먼저 요구사항에서 홀수 번째 노드 다음에 짝수 번째 노드가 와야 한다고 했으므로, 홀수 노드와 짝수 노드를 각각 만들고 홀수 노드의 끝에 짝수 노드를 연결해주면 된다. 먼저 `head`는 홀수 번째이므로 `odd`에, `head.next`는 `even`으로 만들어 주고, 나중에 홀수 노드 끝에 짝수 노드를 연결해주어야 하므로 짝수 노드의 처음을 기억할 `even_head`도 `head.next`로 지정해 준다. 주어진 노드가 끝날 때까지 계속해야 하므로 `while`문을 사용하여 `odd` 노드와 `even`노드를 계속해서 연결해 주고, 마지막에 `odd.next`를 `even_head`로 연결해주면 끝난다. `head`는 여전히 주어진 노드의 처음을 기억하고 있으므로 `head`를 반환해주면 된다.
