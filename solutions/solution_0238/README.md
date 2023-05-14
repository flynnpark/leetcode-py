# 0238. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&id=leetcode-75)

Given an integer array `nums`, return a*n array* `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

### **Example 1:**

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

### **Example 2:**

<pre>
<strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>

### **Constraints:**

- <code>2 <= nums.length <= 10<sup>5</sup></code>
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)
