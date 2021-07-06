# 00234. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given the `head` of a singly linked list, return `true` if it is a palindrome.

#### Example 1:

![](../../images/pal1linked-list.jpg)

<pre><code><strong>Input:</strong> head = [1,2,2,1]
<strong>Output:</strong> true</code></pre>

#### Example 2:

![](../../images/pal2linked-list.jpg)

<pre><code><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> false</code></pre>

#### Constraints:

- The number of nodes in the list is in the range `[1, 10<sup>5</sup>]`.
- `0 <= Node.val <= 9`

## 해결 방법

주어진 단일 연결 리스트가 팰린드롬인지 확인하는 문제이다. 이번 문제는 런너 기법을 사용해서 해결했다. 두 가지 포인터를 사용하는 건데, 빠른 포인터인 `fast`는 2개씩 뒤로 이동하고 느린 포인터인 `slow`는 하나씩 이동한다. `fast`가 마지막 노드에 다다랐을 때, `slow`는 전체 연결 리스트의 중앙에 위치하게 된다. 그리고 남은 노드와 이전 노드들을 비교해서 값이 같은지 확인하면 된다. 이를 위해 `slow`가 중앙으로 이동할 때 거치는 노드들을 역순으로 저장해두고 비교한다. 노드의 길이가 홀수라면 한 노드를 더 이동해서 중앙 값을 피해야 한다. 홀수라면 중앙의 위치한 값은 신경쓰지 않아도 되기 때문이다.
