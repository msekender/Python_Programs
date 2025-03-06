'''
Solution: Regular Expression Matching
We can solve this problem using dynamic programming. The idea is to define a DP table dp[i][j], which represents whether the first i characters of the string s match the first j characters of the pattern p.

Algorithm
Define a 2D DP Table:

dp[i][j] is True if s[0:i] matches p[0:j], otherwise False.
dp[0][0] = True because an empty string matches an empty pattern.
Handle '*' in the pattern:

p[j-1] is *, meaning it can match zero or more of the previous character.
If p[j-2] matches s[i-1] or p[j-2] == '.', we check:
dp[i][j] = dp[i-1][j] (if '*' repeats the preceding character)
dp[i][j] = dp[i][j-2] (if '*' means skipping the preceding character)
Otherwise, dp[i][j] = dp[i][j-2] (skip the preceding character and '*').
Handle '.' and direct character matches:

If p[j-1] == '.' or p[j-1] == s[i-1], then dp[i][j] = dp[i-1][j-1].'
'''

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # DP table where dp[i][j] means s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True

    # Fill the table for patterns with '*'
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # '*' makes preceding character disappear

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':  
                # Exact match or '.' wildcard
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' means zero or more of the preceding element
                dp[i][j] = dp[i][j - 2]  # Case where '*' means remove previous character
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] |= dp[i - 1][j]  # Case where '*' repeats preceding character

    return dp[m][n]

# Example test cases
print(isMatch("aa", "a"))     # False
print(isMatch("aa", "a*"))    # True
print(isMatch("ab", ".*"))    # True

'''
Time Complexity Analysis
We iterate through a 2D DP table of size (m+1) × (n+1), where m = len(s) and n = len(p).
Each cell dp[i][j] takes O(1) time to compute.
Total time complexity: O(m × n)
Given 1 ≤ s.length, p.length ≤ 20, this is highly efficient.

Space Complexity Analysis
The DP table requires O(m × n) extra space.
We can optimize it further using O(n) space by keeping only the previous row.
'''
