# 0030. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150)

You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if words` = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of _the starting indices_ of all the concatenated substrings in `s`. You can return the answer in **any order**.

#### **Example 1:**

<pre><code><strong>Input:</strong> s = "barfoothefoobarman", words = ["foo","bar"]
<strong>Output:</strong> [0,9]
<strong>Explanation:</strong>
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
<strong>Output:</strong> []
<strong>Explanation:</strong>
There is no concatenated substring.
</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
<strong>Output:</strong> [6,9,12]
<strong>Explanation:</strong>
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
</code></pre>

#### **Constraints:**

- <code>1 <= s.length <= 10<sup>4</sup></code>
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters.
