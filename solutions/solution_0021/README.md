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
