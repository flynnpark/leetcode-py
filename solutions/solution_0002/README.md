# 0002. Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#### **Example 1:**

![](../../images/addtwonumber1.jpg)

<pre><code><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]</code></pre>

#### **Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

### 해결방법

Linked List 형태로 입력되는 두 수의 합을 구하여 Linked List 형태로 반환하는 문제. 때문에 입력되는 두 수는 모두 일반적인 숫자 순서를 뒤집어진 상태로 들어온다. 첫 번째 아이템끼리 더하고 두 번째 아이템끼리 더하는 식이다. 뭐 따로 설명할 건 없고 올림수 처리만 잘 하면 될 것 같다. `result`에 더미를 만들기 싫었는데 다른 방법을 생각해내지 못해 더미를 만들어 사용했다.

테스트 코드도 계속 작성하려고 하다 보니 LeetCode 상 예시의 숫자 배열을 `ListNode`로 바꿔주는 코드를 작성하였고, `ListNode` 객체들의 비교를 위해 `__eq__` 함수를 정의하여 작성하였다.
