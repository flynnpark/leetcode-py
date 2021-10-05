## 0024. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#### **Example 1:**

![](../../images/swap_ex1.jpg)

<pre><code><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]</code></pre>

#### **Example 2:**

![](../../images/swap_ex1.jpg)

<pre><code><strong>Input:</strong> head = []
<strong>Output:</strong> []</code></pre>

#### **Example 3:**

![](../../images/swap_ex1.jpg)

<pre><code><strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]</code></pre>

#### **Constraints:**

- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

## 해결 방법

주어진 링크드리스트를 짝 단위로 스왑하고, 그 결과를 반환해야 하는 문제이다. 링크드리스트를 변경해야 하는데, 이 경우 순서가 변경되는 노드 뿐만 아니라 해당 노드들과 연결되어 있는 모든 노드를 수정해야 해서 꽤 복잡하다. 나는 이 문제를 재귀를 통해 해결했다. 먼저 임시 변수 `p`에 `head.next`를 기억해 두고, `p.next`를 인자로 하여 재귀호출하도록 한다. 그리고 나온 결과를 `head.next`에 넣고, `p.next`를 `head`로 변경하고, `p`를 반환한다. 만약 인자로 받은 `head`가 없거나 `head.next`가 없을 경우엔 그대로 `head`를 반환하면 된다. `sawpPairs` 함수에서 `p.next`가 없거나 `p.next.next`가 없을 경우엔 재귀 함수는 동작하지 않는 것이나 마찬가지이므로 `head`와 `head.next`의 순서만 바뀐 게 되므로 이를 계속해서 반복하면 원하는 결과가 나오게 된다.
