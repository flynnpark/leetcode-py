# 0076. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150)

Given two strings `s` and `t` of lengths `m` and `n` respectively, return _the **minimum window substring** of s such that every character in t **(including duplicates)** is included in the window._ If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is `unique`.

### **Example 1:**

<pre><code><strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
<strong>Explanation:</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</code></pre>

### **Example 2:**

<pre><code><strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
<strong>Explanation:</strong> The entire string s is the minimum window.
</code></pre>

### **Example 3:**

<pre><code><strong>Input:</strong> s = "a", t = "aa"
<strong>Output:</strong> ""
<strong>Explanation:</strong> Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
</code></pre>

### **Constraints:**

- `m == s.length`
- `n == t.length`
- <code>1 <= m, n <= 10<sup>5</sup></code>
- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?
