# 1431. [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&id=leetcode-75)

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the <code>i<sup>th</sup></code> kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return _a boolean array_ `result` _of length_ `n`_, where_ `result[i]` _is_ `true` _if, after giving the_ <code>i<sup>th</sup></code> _kid all the_ `extraCandies`_, they will have the greatest number of candies among all the kids, or_ `false` _otherwise_.

Note that multiple kids can have the **greatest** number of candies.

### **Example 1:**

<pre>
<strong>Input:</strong> candies = [2,3,5,1,3], extraCandies = 3
<strong>Output:</strong> [true,true,true,false,true]
<strong>Explanation:</strong> If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
</pre>

### **Example 2:**

<pre>
<strong>Input:</strong> candies = [4,2,1,1,2], extraCandies = 1
<strong>Output:</strong> [true,false,false,false,false]
<strong>Explanation:</strong> There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
</pre>

### **Example 3:**

<pre>
<strong>Input:</strong> candies = [12,1,12], extraCandies = 10
<strong>Output:</strong> [true,false,true]
</pre>

### **Constraints:**

- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`
