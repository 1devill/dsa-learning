# Problem: Product of Array Except Self

# Given an array of integers nums, return a new array output where output[i] is the product of all elements in nums except nums[i].
# You must do it without using division.

# Example:
# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Complexity
# Time: O(n) — two linear passes
# Space: O(1) — only one extra variable running, output array doesn't count

def solution(nums: list[int]) -> list[int]:
    n = len(nums)
    output = []

    running = 1
    for i in range(n):
        output.append(running)
        running = running * nums[i]

    running = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * running
        running = running * nums[i]
        
    return output

print(solution([1, 2, 3, 4]))

# Brute force
# It has O(n) squared time complexity and O(n) space complexity

def brute_force(nums: list[int]) -> list[int]:
    arr = []
    for i in range(len(nums)):
        val = 1
        for index, num in enumerate(nums):
            if index != i:
                val *= num
        arr.append(val)
    return arr



# print(brute_force([1, 2, 3, 4]))
