def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i = len(a) - 1  # Pointer for string a
    j = len(b) - 1  # Pointer for string b
    
    # Process digits from right to left
    while i >= 0 or j >= 0 or carry:
        # Get digits (0 if out of bounds)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        # Compute sum and carry
        total = digit_a + digit_b + carry
        result.append(str(total % 2))  # Current bit
        carry = total // 2             # Carry for next position
        i -= 1
        j -= 1
    
    # Reverse result and join to string
    result = ''.join(result[::-1])
    # Handle case where result is empty or "0"
    return result if result else "0"

print(addBinary("100", "1"))
print(addBinary("11", "1"))
print(addBinary("1", "0"))
