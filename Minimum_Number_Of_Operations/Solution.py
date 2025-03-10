'''
Left-to-Right Pass:

Track the number of balls (left_count) and their cumulative operations (left_moves).
Store operations required to bring all left-side balls to each index.
Right-to-Left Pass:

Similarly, track the number of balls (right_count) and cumulative operations (right_moves).
Update the answer array by adding the contributions from the right.
'''

def minOperations(boxes: str):
    n = len(boxes)
    answer = [0] * n
    left_count, left_moves = 0, 0

    # Left-to-right pass
    for i in range(n):
        answer[i] = left_moves
        if boxes[i] == '1':
            left_count += 1
        left_moves += left_count

    right_count, right_moves = 0, 0

    # Right-to-left pass
    for i in range(n - 1, -1, -1):
        answer[i] += right_moves
        if boxes[i] == '1':
            right_count += 1
        right_moves += right_count

    return answer

# Example test cases
print(minOperations("110"))     # Output: [1, 1, 3]
print(minOperations("001011"))  # Output: [11, 8, 5, 4, 3, 4]

'''
Time Complexity Analysis
First pass (Left-to-Right):
Iterates through the string once (O(n)) and computes the cumulative operations.
Second pass (Right-to-Left):
Again, iterates through the string once (O(n)).
Total complexity:
O(n) + O(n) = O(n), which is efficient for n ≤ 2000.

Space Complexity Analysis
Uses an output array of size n → O(n).
Only a few additional integer variables (left_count, left_moves, right_count, right_moves) → O(1).
Overall space complexity: O(n) (due to the output array).'
'''