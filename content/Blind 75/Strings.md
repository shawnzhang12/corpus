---
title: "Strings"
weight: -20
---

### Validate Palindrome :green_book:

##### Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

##### Solution

Use regex expressions for speed. Lower the string, remove non-alphanumeric, and compare with backwards version for answer.

`r'[^0-9a-zA-Z]'` is an equivalent of saying replace everything that's NOT from 0-9, a-z, or A-Z, notice the `^` is in the square brackets. `'[\W_]+'` means replace any one or more consecutive non-word characters or underscores. The `+` seems to make it run a bit faster for test cases with long strings of non-alphanumeric characters. `r` prefix is used to remove escape sequences such as `\r \n \t \s` to two characters each - a backslash and a letter. 

Time Complexity: O(n)

Space Complexity: O(1)

```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = re.sub(r'[\W_]+', '', s.lower())
        return processed_s == processed_s[::-1]
```

