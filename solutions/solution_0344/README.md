# 0344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

You may assume all the characters consist of [printable ascii characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

#### Example 1:

<pre><code><strong>Input:</strong> ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]</code></pre>

#### Example 2:

<pre><code><strong>Input:</strong> ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]</code></pre>

## 해결방법

1번 방법은 투 포인터를 이용한 방식으로 두 개의 포인터의 위치를 옮겨가면서 위치만 옮겨주는 방식이다.

2번 방법은 그냥 리스트의 `reverse()` 함수를 통해 뒤집은 방법이다.
