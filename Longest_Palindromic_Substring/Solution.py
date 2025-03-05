''' 
Solution using Expand Around Center Approach (Optimal Approach):
We can solve this problem efficiently using the Expand Around Center technique.

Key Idea:
A palindrome expands equally around its center.
We check all possible centers (both single-character and two-character centers) and expand outward while characters match.
Track the longest palindrome found during the process.
'''

class LongestPalindromicSubstring:
    def __init__(self, s: str):
        self.s = s

    def expand_around_center(self, left: int, right: int) -> str:
        """Expands around the center and returns the longest palindrome found."""
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        return self.s[left + 1:right]  # Extract the valid palindrome

    def longest_palindrome(self) -> str:
        if not self.s or len(self.s) == 1:
            return self.s

        longest = ""
        for i in range(len(self.s)):
            # Check for odd-length palindromes (single character center)
            odd_palindrome = self.expand_around_center(i, i)
            # Check for even-length palindromes (two-character center)
            even_palindrome = self.expand_around_center(i, i + 1)

            # Update longest palindrome found
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# Example Usage
solver = LongestPalindromicSubstring("babad")
print(solver.longest_palindrome())  # Output: "bab" or "aba"

solver2 = LongestPalindromicSubstring("cbbd")
print(solver2.longest_palindrome())  # Output: "bb"


''' 
How It Works:
Iterate through each index i in the string as a potential center.
Expand outward to check:
Odd-length palindromes (centered at i).
Even-length palindromes (centered between i and i+1).
Keep track of the longest palindrome found.

Complexity Analysis:
Time Complexity: O(n²)
Each character is treated as a center, and in the worst case, we expand up to O(n) times.
Total complexity is O(n × n) = O(n²).
Space Complexity: O(1)
We only use a few variables (no extra arrays), so space usage is constant.
'''