# 0005. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string `s`, return _the longest palindromic substring_ in `s`.

#### Example 1:

<pre><code><strong>Input: s = "babad"</strong>
<strong>Output:</strong> "bab"
<strong>Note:</code> "aba" is also a valid answer.</pre>

#### Example 2:

<pre><code><strong>Input: s = "cbbd"</strong>
<strong>Output:</strong> "bb"</code></pre>

#### Example 3:

<pre><code><strong>Input: s = "a"</strong>
<strong>Output:</strong> "a"</code></pre>

#### Example 4:

<pre><code><strong>Input: Input: s = "ac"</strong>
<strong>Output:</strong> Output: "a"</code></pre>

#### Constraints:

- `1 <= s.length <= 1000`
- `s` consist of only digit and english letters (lower-case and/or upper-case)

## 해결 방법

이전에 한 번 풀었었던 팰린드롬에 대한 문제이다. 그 때는 해당 문자열이 팰린드롬인지 판별하는 함수를 작성하는 거였는데, 이번에는 주어진 문자열에서 가장 긴 팰린드롬을 찾는 문제이다.

문자열 내에서 팰린드롬을 찾기 위해서는 먼저 가장 작은 단위의 팰린드롬부터 찾아야 하는데, 문자 하나 하나는 자체적으로 팰린드롬이나 다름 없기 때문에 제외하고, 문자 2개가 같거나, 한 문자의 앞 문자와 뒤 문자가 같은 경우 각각 팰린드롬이라고 볼 수 있다. 따라서 문자열을 차례대로 돌면서 해당 문자를 포함한 2개의 문자 또는 3개의 문자가 팰린드롬인지 확인하고, 만약 팰린드롬일 경우 그 문자열의 앞뒤로 하나씩 넓혀가면서 팰린드롬인지 확인하고 가장 긴 팰린드롬의 결과를 반환해야 한다.

먼저, 문자열의 길이가 1인 경우와 문자열 자체가 팰린드롬인 경우는 바로 해당 문자열을 반환하고, 아닐 경우엔 문자열 내부에서 팰린드롬을 찾는다. 팰린드롬인지 확인하는 내부 함수인 `check`는 `left`와 `right`를 인덱스로 받으며, `s[left]`와 `s[right]`가 같은 문자일 경우 팰린드롬으로 간주한다. 이유는 2개의 문자 또는 3개의 문자가 팰린드롬인지 먼저 확인을 하기 때문이다. 그리고 팰린드롬일 경우엔 `left`는 하나씩 줄이고, `right`는 하나씩 늘려가면서 추가적인 확인을 진행한다.

다음으로 해당 문자열 내에서 가장 긴 팰린드롬을 찾아야 하는데, 이는 간단히 `max` 함수를 통해 해결할 수 있다. `key`를 길이를 비교하는 `len`으로 두고, 짝수 문자 팰린드롬을 비교하는 함수의 결과, 홀수 문자 팰린드롬을 비교하는 결과와 이전 팰린드롬 결과를 비교해서 간단하게 가지고 올 수 있다.
