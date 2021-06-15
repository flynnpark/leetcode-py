# 0020. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

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

## 해결 방법

괄호들이 유효한지를 판별하는 프로그램을 작성해야 했다. 각 괄호들이 유효하기 위해서는 한 번 열린 괄호는 반드시 닫혀야 하고, 해당 괄호가 닫히기 전에 이전에 입력된 괄호가 닫혀서는 안 된다.

먼저 괄호는 쌍이 있기 때문에 `dict`로 괄호 쌍을 선언했다. 입력된 문자열을 돌면서 현재 순서의 괄호가 왼쪽 쌍일 경우엔 `stack`이라는 이름의 `list`에 담고, 오른쪽 쌍일 경우엔 해당 괄호의 오른쪽 쌍이 `stack`의 맨 마지막에 있는 괄호랑 쌍이 맞는지 판별하도록 하였다. 쌍이 맞을 경우 해당 활호의 쌍은 `stack`에서도 제거 된다. 그리고 괄호의 오른쪽 쌍을 판별하는데 `stack`에 아무 것도 없을 때나 문자열을 다 돌았는데도 `stack`에 괄호가 남아 있다면 유효하지 않으므로 `False`를 반환하고, 아닐 경우엔 `True`를 반환하도록 하였다.
