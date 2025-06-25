
def is_correct_capitalization(word):
        
    """
        Checks whether the word uses capitalization correctly.
        Rules:
        - All letters are capitalized
        - All letters are lowercase
        - Only the first letter is capitalized
        
    """
        
    return (
            word.isupper() or
            word.islower() or
            (word[0].isupper() and word[1:].islower())
        )


#  Test cases
if __name__ == "__main__":
    test_cases = [
        ("USA", True),
        ("Calvin", True),
        ("compUter", False),
        ("coding", True),
        ("C", True),
        ("c", True),
        ("uSA", False)
    ]

    for word, expected in test_cases:
        result = is_correct_capitalization(word)
        assert result == expected, f"Failed for {word}: expected {expected}, got {result}"
    print("All test cases passed ✅")

# print(is_correct_capitalization("USA"))      # True
# print(is_correct_capitalization("Calvin"))   # True
# print(is_correct_capitalization("compUter")) # False
# print(is_correct_capitalization("coding"))   # True
