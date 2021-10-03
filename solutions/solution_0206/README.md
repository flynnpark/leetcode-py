## 0206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

#### **Example 1:**

![](../../images/reverse-linked-list-1.jpg)

<pre><code><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]</code></pre>

#### **Example 2:**

![](../../images/reverse-linked-list-2.jpg)

<pre><code><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> head = []
<strong>Output:</strong> []</code></pre>

#### **Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## 해결 방법

주어진 링크드리스트를 뒤집는 문제이다. 여기서는 `node.next`를 `prev`로 계속 연결하는 방식으로 간단하게 해결했다. `node`를 `head`로, `prev`를 `None`으로 초깃값을 정해준 후, `node.next`를 `next`에 임시 저장하고, `node.next`를 `prev`로 교체한다. 그 이후 `node`를 `prev`에 임시 저장하고, 이전에 저장한 `next`(원래의 `node.next`)를 `node`로 교체한다. 이를 `node`가 존재하지 않을때까지 계속해서 반복하면 된다.
