Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)

## Solution Approach

Idea: Use a hash set to store numbers we’ve seen. For each number, check if k - nums[i] exists in the set.

Why it works: If nums[i] + nums[j] == k, then nums[j] == k - nums[i]. By checking if k - nums[i] is in the set, we can find a pair in O(1) per element.

Handling the constraint: Since we can’t sum a number with itself, we check for k - nums[i] before adding nums[i] to the set, ensuring we’re looking at a previously seen number.

## Steps:

- Initialize an empty hash set.

- Iterate through the array:
_For each nums[i], compute the complement k - nums[i]._

_If the complement exists in the set, we’ve found a pair → return true._

_Add nums[i] to the set._

_If no pair is found, return false._

Time Complexity: O(n) (single pass through the array, with O(1) hash operations).
Space Complexity: O(n) (to store up to n elements in the set).

