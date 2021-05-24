# 0049. Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### Example 1:

<pre><code><strong>Input:</strong> ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]</code></pre>

#### Example 3:

<pre><code><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]</code></pre>

#### Constraints:

- <code>1 <= strs.length <= 10<sup>4</sup></code>
- <code>0 <= strs[i].length <= 100</code>
- <code>strs[i]</code> consists of lower-case English letters.