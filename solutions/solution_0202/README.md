# 0202. [Happy Number](https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150)

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in** 1 are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not._

### **Example 1:**

<pre><code><strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</code></pre>

### **Example 2:**

<pre><code><strong>Input:</strong> n = 2
<strong>Output:</strong> false
</code></pre>

### **Constraints:**

- <code>1 <= n <= 2<sup>31</sup> - 1</code>
