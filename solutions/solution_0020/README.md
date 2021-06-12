# 0049. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

#### Example 1:

<pre><code><strong>Input:</strong> s = "()"
<strong>Output:</strong> true</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> "()[]{}"
<strong>Output:</strong> true</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> s = "(]"
<strong>Output:</strong> false</code></pre>

#### Example 4:

<pre><code><strong>Input:</strong> s = "([)]"
<strong>Output:</strong> false</code></pre>

#### Example 5:

<pre><code><strong>Input:</strong> s = "{[]}"
<strong>Output:</strong> true</code></pre>

#### Constraints:

- `1 <= s.length <= 10<sup>4</sup>`
- `s` consists of parentheses only `'()[]{}'`.
