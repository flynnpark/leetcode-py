## 0561. [Array Partition](https://leetcode.com/problems/array-partition/)

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (a<sub>n</sub>, b<sub>n</sub>)` such that the sum of `min(a<sub>i</sub>, b<sub>i</sub>)` for all `i` is **maximized**. Return _the maximized sum_.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [1,4,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [6,2,6,5,1,2]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.</code></pre>

#### **Constraints:**

- `1 <= n <= 10<sup>4</sup>`
- `nums.length == 2 * n`
- `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`
