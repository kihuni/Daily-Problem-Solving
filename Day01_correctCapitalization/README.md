# Day 01 - Correct Capitalization

### ✅ Problem

Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if:

1. All letters are capitalized (`"USA"`)
2. No letters are capitalized (`"coding"`)
3. Only the first letter is capitalized (`"Calvin"`)

Otherwise, return false (`"compUter"`).

### Examples

```
Input: "USA"       → Output: True  
Input: "Calvin"    → Output: True  
Input: "compUter"  → Output: False  
Input: "coding"    → Output: True 

```
### Approach

- Check if the entire word is uppercase using isupper()

- Check if the entire word is lowercase using islower()

- Check if only the first letter is uppercase and the rest lowercase using slicing