# 0021. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a `sorted` list. The list should be made by splicing together the nodes of the first two lists.

#### Example 1:

![](../../images/merge_ex1.jpg)

<pre><code><strong>Input:</strong> l1 = [1,2,4], l2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> l1 = [], l2 = []
<strong>Output:</strong> []</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> l1 = [], l2 = [0]
<strong>Output:</strong> [0]</code></pre>

#### Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.

## 해결 방법

예전에 풀었던 `Two Sum`과 비슷한 유형의 문제이다. 단지 정렬된 두 숫자의 배열을 정렬된 하나의 배열로 만들기만 하면 되었기 때문에 비교하는 방법만 조금 달랐다. 빈 배열을 먼저 하나 만들고, 각 배열을 하나씩 보면서 `l1` 배열의 값이 작을 경우 `l1`의 값을 빈 배열에 넣고, `l2`의 배열의 값이 작을경우 `l2`의 배열의 값을 넣고. 둘 중 한 배열이 완전히 비어 있을 경우엔 남은 배열을 그대로 붙여주기만 하면 되었다.

풀고 나니 왠지 재귀호출로도 풀 수 있는 방법이 있을 것 같아서, 하나 추가로 구현해 보았다. 덕분에 빈 배열을 만들지 않고도 해결할 수 있게 되었다.
