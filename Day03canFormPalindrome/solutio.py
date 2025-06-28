def canFormPalindrome(s: str) -> bool:
    def isPalindrome(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Try deleting character at left or right
            return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
    return True


print(canFormPalindrome("abcba"))
print(canFormPalindrome("foobof"))
print(canFormPalindrome("abccab"))