# 0334. [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&id=leetcode-75)

Given an integer array `nums`, return `true` _if there exists a triple of indices_ `(i, j, k)` _such that_ `i < j < k` _and_ `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

### **Example 1:**

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Any triplet where i < j < k is valid.
</pre>

### **Example 2:**

<pre>
<strong>Input:</strong> nums = [5,4,3,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> No triplet exists.
</pre>

### **Example 3:**

<pre>
<strong>Input:</strong> nums = [2,1,5,0,4,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
</pre>

### **Constraints:**

- <code>1 <= nums.length <= 5 \* 10<sup>5</sup></code>
- <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
