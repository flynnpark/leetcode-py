## 0029. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return _the **quotient** after dividing_ `dividend` by `divisor`.

**Note:** Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[−2<sup>31</sup>, 2<sup>31</sup> − 1]`. For this problem, if the quotient is **strictly greater than** `2<sup>31</sup> - 1`, then return `2<sup>31</sup> - 1`, and if the quotient is **strictly less** than `-2<sup>31</sup>`, then return `-2<sup>31</sup>`.

#### **Example 1:**

<pre><code><strong>Input:</strong> dividend = 10, divisor = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10/3 = 3.33333.. which is truncated to 3.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> dividend = 7, divisor = -3
<strong>Output:</strong> -2
<strong>Explanation:</strong> 7/-3 = -2.33333.. which is truncated to -2.</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> dividend = 0, divisor = 1
<strong>Output:</strong> 0</code></pre>

#### **Example 4:**

<pre><code><strong>Input:</strong> dividend = 1, divisor = 1
<strong>Output:</strong> 1</code></pre>

#### **Constraints:**

- `-2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1`
- `divisor != 0`
