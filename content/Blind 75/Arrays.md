---
title: "Arrays"
weight: -20
---

### Two Sum  :green_book:

##### Problem

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*. You may assume that each input would have ***exactly*** **one solution**, and you may not use the *same* element twice. You can return the answer in any order.

##### Solution

The concept here is to have a dictionary that stores the current value and the key, and the index as the value. This way as we iterate through the list, we can check if the difference already exists in the dictionary. If it does, then we found our answer and return the indices. Otherwise, add the current value and index to the dictionary.

Time Complexity: O(n)

Space Complexity: O(n)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return None  # No solution found
```

### Best Time to Buy and Sell Stock :green_book:

##### Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock. Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

##### Solution

We want to keep track of the minimum price so far as we iterate through the prices. This will be the "buy" point. If the current price is the minimum price, then we should forget about selling (that's how you lose money). Now if it's not the minimum, we can determine a profit margin by comparing the current price with the minimum. If the profit margin is higher than previous profit margins than we keep this one as our "sell" point for most money. 

Time Complexity: O(n)

Space Complexity: O(1)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit	
```

