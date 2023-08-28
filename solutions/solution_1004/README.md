# 1004. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&id=leetcode-75)

Given a binary array `nums` and an integer `k`, return _the maximum number of consecutive_ `1`_'s in the array if you can flip at most_ `k` `0`_'s._

### **Example 1:**

<pre>
<strong>Input:</strong> nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> [1,1,1,0,0,<strong>1</strong>,1,1,1,1,<strong>1</strong>]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
</pre>

### **Example 2:**

<pre>
<strong>Input:</strong> nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> [0,0,1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
</pre>

### **Constraints:**

- <code>1 <= nums.length <= 10<sup>5</sup></code>
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`
