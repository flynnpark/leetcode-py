# 0015. [3Sum](https://leetcode.com/problems/3sum/)

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

#### Example 1:

<pre><code><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> nums = []
<strong>Output:</strong> []</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> nums = [0]
<strong>Output:</strong> []</code></pre>

#### Constraints:

- `0 <= nums.length <= 3000`
- `-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>`
