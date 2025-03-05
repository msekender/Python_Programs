'''
Solution using Sliding Window (Optimized Approach):
We can solve this problem efficiently using the Sliding Window technique with 
a HashSet (or HashMap) to track characters in the current substring.
'''

class LongestSubstring:
    def __init__(self, s: str):
        self.s = s

    def length_of_longest_substring(self) -> int:
        char_set = set()  # Stores unique characters in the current window
        left = 0  # Left pointer of the window
        max_length = 0  # Stores the max length of substring

        for right in range(len(self.s)):
            while self.s[right] in char_set:
                char_set.remove(self.s[left])
                left += 1  # Shrink window from the left

            char_set.add(self.s[right])  # Expand window to the right
            max_length = max(max_length, right - left + 1)

        return max_length

# Example Usage
solver = LongestSubstring("abcabcbb")
print(solver.length_of_longest_substring())  # Output: 3

solver2 = LongestSubstring("bbbbb")
print(solver2.length_of_longest_substring())  # Output: 1

solver3 = LongestSubstring("pwwkew")
print(solver3.length_of_longest_substring())  # Output: 3

'''
How It Works:
Two pointers (left, right) are used to maintain a sliding window.
Expand the window by adding s[right] to a set (ensuring unique characters).
If s[right] already exists in the set, shrink the window from the left side until s[right] becomes unique again.
Keep track of the maximum length found.

Complexity Analysis:
Time Complexity: O(n)
Each character is processed at most twice (once when added and once when removed), leading to linear time complexity.
Space Complexity: O(min(n, m))
O(m), where m is the size of the character set (e.g., 26 for lowercase letters or 128 for ASCII characters).
'''