## 0316. [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

#### **Example 1:**

<pre><code><strong>Input:</strong> s = "bcabc"
<strong>Output:</strong> "abc"</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> s = "cbacdcbc"
<strong>Output:</strong> "acdb"</code></pre>

#### **Constraints:**

- `1 <= s.length <= 10<sup>4</sup>`
- `s` consists of lowercase English letters.

## 해결 방법

주어진 문자열 `s`에서 중복되는 문자를 제거해야 하는데, 제거한 결과가 모든 경우 대비 사전순으로 가장 빨라야 한다. `bcabc`라는 문자열이 주어졌다면, 중복되는 문자 `b`와 `c`를 제거하는 경우에서, `bca`, `bac`, `cab`보다 `abc`가 사전순으로 가장 빠르므로, 결과는 `abc`가 되어야 하는 것이다. 이를 위해서 `Counter` 클래스와 리스트를 사용하였다. `Counter` 클래스 사용하면 주어진 문자열을 문자별로 카운트할 수 있다. 먼저 주어진 문자열 `s`를 순회하면서 `counter`에 기록되어 있는 해당 문자의 사용 숫자를 1 줄이면서 문자를 `stack` 리스트에 집어 넣는다. 이 때, 해당 문자가 `stack`에 이미 존재하면 넘어간다. 그리고 해당 문자가 `stack`의 마지막 문자보다 사전순으로 빠르고, 아직 `counter`에 있는 해당 문자의 값이 0을 넘는다면 해당 문자를 `stack`에서 삭제한다. 이를 계속 반복하면 `stack`에는 사전순으로 빠르고 중복되지 않은 문자만이 남는다.
