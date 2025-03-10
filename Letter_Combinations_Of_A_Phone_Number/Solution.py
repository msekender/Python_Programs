/*
Solution Approach:
We use backtracking to generate all possible letter combinations.
We define a mapping of digits (2-9) to their respective letter groups.
We recursively explore all possible letter combinations for the given digits.
*/

def letter_combinations(digits):
    if not digits:
        return []
    
    # Mapping of digits to letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    result = []
    
    # Backtracking function
    def backtrack(index, current):
        # Base case: if the combination is complete
        if index == len(digits):
            result.append(current)
            return
        
        # Get possible letters for the current digit
        letters = phone_map[digits[index]]
        
        # Iterate through the letters and recurse
        for letter in letters:
            backtrack(index + 1, current + letter)
    
    # Start backtracking from index 0
    backtrack(0, "")
    
    return result

# Example test cases
print(letter_combinations("23"))  # Expected Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations(""))    # Expected Output: []
print(letter_combinations("2"))   # Expected Output: ["a", "b", "c"]

/* 
Complexity Analysis
Time Complexity:
Each digit in the input string can represent 3 or 4 letters.
If there are n digits, the total number of combinations is approximately:
3ⁿ to 4ⁿ possible combinations.
Since we generate all combinations recursively, the worst-case time complexity is:
O(4ⁿ) (since the digit '7' and '9' map to 4 letters, while others map to 3).
Given that n ≤ 4, the worst case is 4⁴ = 256, which is manageable.

Space Complexity:
The space required for storing the result is O(4ⁿ) in the worst case.
The recursive call stack depth is O(n) due to backtracking.
Total Space Complexity: O(4ⁿ + n) ≈ O(4ⁿ).
*/
