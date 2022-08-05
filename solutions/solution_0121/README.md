## 0121. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i<sup>th</sup>` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

#### **Example 1:**

<pre><code><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.</code></pre>

#### **Example 2:**

<pre><code><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.</code></pre>

#### **Constraints:**

- `1 <= prices.length <= 10<sup>5</sup>`
- `0 <= prices[i] <= 10<sup>4</sup>`

## 해결 방법

`i`번째 일의 주식 가격 정보를 담고 있는 `prices` 배열이 주어지고, 한 번의 거래로 낼 수 있는 최대 이익을 찾는 문제이다. 쉽게 생각하면 저점에 사서 고점에 팔면 된다.

여기서는 간단하게 `min_price`라는 변수를 사용하여 `prices` 배열을 순회하면서 최소 가격을 업데이트 하고, 현재 가격 `price`와 현재 시점의 최소 가격 `min_price`의 차이를 계산하여 최대 이익을 수하도록 계산했다.
