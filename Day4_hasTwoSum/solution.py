def hasTwoSum(nums: list[int], k: int) -> bool:
    seen = set()
    for num in nums:
        complement = k - num
        if complement in seen:
            return True
        seen.add(num)
    return False


print(hasTwoSum([1, 3, 8, 2], k = 10))
print(hasTwoSum([3, 9, 13, 7], k = 8))
print(hasTwoSum([4, 2, 6, 5, 2], k = 4))