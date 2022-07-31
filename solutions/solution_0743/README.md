## 0743. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)`, where `u<sub>i</sub>` is the source node, `v<sub>i</sub>` is the target node, and `w<sub>i</sub>` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the `n` nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

#### **Example 1:**

![](../../images/0743.jpg)

<pre><code><strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1</code></pre>

#### **Example 3:**

<pre><code><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1</code></pre>

#### **Constraints:**

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u<sub>i</sub>, v<sub>i</sub> <= n`
- `u<sub>i</sub> != v<sub>i</sub>`
- `0 <= w<sub>i</sub> <= 100`
- All the pairs `(u<sub>i</sub>, v<sub>i</sub>)` are **unique**. (i.e., no multiple edges.)
