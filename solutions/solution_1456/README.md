# 1456. [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&id=leetcode-75)

Given a string `s` and an integer `k`, return _the maximum number of vowel letters in any substring of_ `s` _with length_ `k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### **Example 1:**

<pre>
<strong>Input:</strong> s = "abciiidef", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring "iii" contains 3 vowel letters.
</pre>

### **Example 2:**

<pre>
<strong>Input:</strong> s = "aeiou", k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>

### **Example 3:**

<pre>
<strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> "lee", "eet" and "ode" contain 2 vowels.
</pre>

### **Constraints:**

- <code>1 <= s.length <= 10<sup>5</sup></code>
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`
