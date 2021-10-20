# 0739. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Given an array of integers `temperatures` represents the daily temperatures, return _an array_ `answer` _such that_ `answer[i]` _is the number of days you have to wait after the_ `i<sup>th</sup>` _day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

#### **Example 1:**

<pre><code><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]</code></pre>

#### **Constraints:**

- `1 <= temperatures.length <= 10<sup>5</sup>`
- `30 <= temperatures[i] <= 100`

## 해결 방법

주어진 온도 리스트에서 `i`번째 날보다 더 따뜻한 날씨를 위해서 며칠을 더 기다려야 하는지를 찾는 문제이다. 만약 `[73,74,75,71,69,72,76,73]`에서 첫 번째 날의 온도인 73도보다 더 따뜻한 날씨를 위해서 기다려야 하는 날은 하루만 기다리면 된다.

테스트케이스에서, 더 따뜻한 날이 없는 경우는 모두 `0`으로 처리되었기 때문에, 결과를 `0`의 배열로 먼저 만들어 준다. 그리고 날짜 계산을 위한 `stack`을 빈 배열로 만들고, `temperatures`를 `enumerate`를 사용하여 순회하면서 `stack`에 인덱스를 기록한다. 이 때, 인덱스를 기록하기 전에 현재 순서의 온도 `temperature`가 `temperatures[stack[-1]]`보다 높을 경우 `result[stack[-1]]`에 현재 날짜 `i`와 `stack[-1]`의 차를 기록한다. `temperature`가 74인 경우를 기준으로 보자면 `stack[-1]`은 0이고, `temperatures[stack[-1]]`(73)은 `temperature`보다 작으므로, `result[0]`은 `i - stack[-1]`의 값인 1이 되는 것이다. 마찬가지로 `temperature`가 76인 경우엔 `stack`이 `[2, 5]`의 값을 가지게 있게 되므로, `result[5]`는 1, `result[2]`는 4가 된다.
