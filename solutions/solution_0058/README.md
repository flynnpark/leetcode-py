# 0058. [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Given a string `s` consists of some words separated by spaces, return _the length of the last word in the string. If the last word does not exist, return_ `0`.

A **word** is a maximal substring consisting of non-space characters only.

#### Example 1:

<pre><code><strong>Input:</strong> s = "Hello World"
<strong>Output:</strong> 5</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> s = " "
<strong>Output:</strong> 0</code></pre>

#### Constraints:

- `1 <= s.length <= 10<sup>4</sup>`
- `s` consists of only English letters and spaces `' '`.

## 해결 방법

별로 어려운 문제가 아니어서 쉽게 풀었다. 주어진 문자열에서 마지막 단어의 길이를 구하는 문제인데, 단어가 없을 경우엔 0을 반환해야 한다. 때문에 문자열이 비어 있거나, 공백을 제거하였을 때 아무 것도 남아 있지 않다면 0을 반환하고 그렇지 않을 경우엔 문자열의 마지막 문자의 길이를 반환하면 된다.
