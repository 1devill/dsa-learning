# Problem: Palindrome

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.
# Return True or False.

# Input:  "A man, a plan, a canal: Panama"
# Output: True

# Input:  "race a car"
# Output: False

# Time complexity — O(n)
# Each character in the string is visited at most once. The left pointer only moves right, the right pointer only moves left,
# and they never backtrack. So in the worst case you traverse the entire string once — that's linear, O(n).

# Space complexity — O(1)
# Look at what your function stores: two integers, left and right. That's it. No new strings, no lists, no hashmaps.
# The memory your function uses does not grow with the size of the input — it's constant regardless
# of whether the string has 10 characters or 10 million. That's O(1).
# This is why moving .lower() to the comparison step was the right call — the previous version created
# a full copy of the string, making it O(n) space.

def solution(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True



print(solution("A man, a plan, a canal: Panama"))
print(solution("race a car"))

# One liner with built in methods
# filtered is O(n) space — violates the O(1) constraint
# filtered[::-1] creates another O(n) string — so you're actually at O(n) space twice over

def built_in(s: str) -> bool:
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]