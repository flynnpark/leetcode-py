## 0092. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return _the reversed list_.

#### **Example 1:**

![](../../images/rev2ex2.jpg)

<pre><code><strong>Input:</strong> head = [1,2,3,4,5], left = 2, right = 4
<strong>Output:</strong> [1,4,3,2,5]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> head = [5], left = 1, right = 1
<strong>Output:</strong> [5]</code></pre>

#### **Constraints:**

- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## 해결 방법

주어진 링크드리스트에서 주어진 위치 `left`와 `right` 사이에 있는 노드들만 역순으로 뒤집는 문제이다. 먼저 주어진 노드 `head`가 존재하지 않거나 `left`와 `right`의 값이 같은 경우를 처리해주고 시작한다.

`new_head`에 더미로 쓰일 노드를 하나 만들고, 기존의 `head`를 연결해 준다. 그리고 기준으로 쓰일 `start`와 `end`를 설정한다. 이 두 노드의 값은 변하지 않는다. 다음으로 반복문을 통해 `left`와 `right` 사이의 노드를 뒤집어 준다. 마지막으로 `new_head.next`를 리턴해 주면 된다. 중간에 반복문을 통해서 노드를 뒤집는 부분은 직접 그림을 그려서 진행해보면 편하다.
