''' 
Approach
Sort the array:

Sorting helps efficiently skip duplicate quadruplets.
Use two nested loops for the first two numbers (i and j):

Fix nums[i] and nums[j] and use two-pointer approach to find nums[c] and nums[d] that sum up to target - (nums[i] + nums[j]).
Use a two-pointer approach for the remaining two numbers (c and d):

Initialize c = j + 1 and d = len(nums) - 1.
Move the pointers based on their sum relative to the target.
Skip duplicates:

If nums[i] == nums[i-1], continue to avoid duplicate quadruplets.'
'''

def fourSum(nums, target):
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate `i`
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicate `j`
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            # Two-pointer approach
            c, d = j + 1, n - 1
            while c < d:
                total = nums[i] + nums[j] + nums[c] + nums[d]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[c], nums[d]])
                    
                    # Move pointers and avoid duplicates
                    while c < d and nums[c] == nums[c + 1]:
                        c += 1
                    while c < d and nums[d] == nums[d - 1]:
                        d -= 1
                    
                    c += 1
                    d -= 1
                
                elif total < target:
                    c += 1  # Need a bigger sum
                else:
                    d -= 1  # Need a smaller sum

    return result

# Example test cases
print(fourSum([1, 0, -1, 0, -2, 2], 0))   # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2, 2, 2, 2, 2], 8))         # Output: [[2,2,2,2]]

'''
Time Complexity Analysis
The number of possible combinations is determined by the product of choices for each digit.
For a digit string of length n:
Each digit has at most 4 choices (7 and 9 have 4 letters, others have 3).
The worst case (digits = "9999") generates 4⁴ = 256 combinations.
Time Complexity: O(4ⁿ) (exponential growth with input length).

Space Complexity Analysis
The result list holds O(4ⁿ) combinations.
The recursive stack has depth O(n).
Total Space Complexity: O(4ⁿ + n) ≈ O(4ⁿ).
'''
