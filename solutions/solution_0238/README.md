## 0238. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

#### **Example 1:**

<pre><code><strong>Input:</strong> nums = [1, 2, 3, 4]
<strong>Output:</strong> [24, 12, 8, 6]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> nums = [-1, 1, 0, -3, 3]
<strong>Output:</strong> [0, -1, -3, 0, 6]</code></pre>

#### **Constraints:**

- `2 <= nums.length <= 10<sup>5</sup>`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
