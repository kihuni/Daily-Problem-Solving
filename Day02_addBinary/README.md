## ✅ Problem Summary

Given two binary strings a and b:

- Return their sum as a binary string.

- Binary strings contain only '0' or '1'.

- No leading zeros (except for "0" itself).

✅ Examples
```
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"

``` 
🧠 Solution Approach

We’ll implement a solution that:
- Iterates through both strings from right to left using indices.

- Computes the sum and carry for each position.

- Builds the result string and reverses it at the end.

- Handles the final carry and removes leading zeros if needed.

