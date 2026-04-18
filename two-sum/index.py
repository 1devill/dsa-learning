# Problem: Two Sum

# Given a list of integers nums and an integer target, return the indices of the two numbers that add up to target.
# You may assume exactly one solution exists, and you cannot use the same element twice.

# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]   # because nums[0] + nums[1] = 2 + 7 = 9

# This solution has O(n) for time complexity because we loop through each element of array
# And O(n) for space complexity because in worst case scenario seen can grow to the nums length

def solution(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[num] = index


print(solution([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))

# Brute force approach
# Time: O(n²) — for each of n elements, you potentially scan n elements.
# Space: O(1) — you store nothing extra.

def brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(brute_force([2, 7, 11, 15], 9))
print(brute_force([3, 2, 4], 6))