---
title: "Arrays"
weight: -20
---

### Two Sum  :green_book:

##### Problem

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*. 

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

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



