/*
Corrected Approach
Sliding Window (Two-Pointer Technique):
Use two pointers (left and right) to maintain a valid window that contains:
All vowels at least once.
Exactly k consonants.
Use a vowel frequency map to track vowels.
Use consonantCount to track consonants.
Count Valid Substrings Properly:
Once a valid window is found (consonantCount == k and all vowels exist):
Count substrings starting from left.
Increment left cautiously, ensuring we still have a valid substring.
*/

def count_substrings(word: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    n = len(word)
    
    left, consonant_count, total_count = 0, 0, 0

    for right in range(n):
        char = word[right]

        # Update vowel frequency
        if char in vowels:
            vowel_count[char] += 1
        else:
            consonant_count += 1  # Update consonant count

        # Shrink left pointer if consonant count exceeds k
        while consonant_count > k:
            if word[left] in vowels:
                vowel_count[word[left]] -= 1
            else:
                consonant_count -= 1
            left += 1

        # If all vowels are present at least once and consonants are exactly k
        if all(vowel_count[v] > 0 for v in "aeiou") and consonant_count == k:
            total_count += 1

    return total_count

# Example test cases
print(count_substrings("aeioqq", 1))        # Output: 0
print(count_substrings("aeiou", 0))         # Output: 1
print(count_substrings("ieaouqqieaouqq", 1)) # Output: 3

'''
Time Complexity Analysis
Expanding right pointer:
Iterates over the string once → O(n).
Shrinking left pointer:
Each character is processed at most once when shrinking → O(n).
Checking vowel presence:
Checking all 5 vowels takes O(1).
Total Time Complexity:
O(n) + O(n) + O(1) = O(n).
'''
