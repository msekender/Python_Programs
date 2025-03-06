def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        width = right - left
        min_height = min(height[left], height[right])
        max_water = max(max_water, width * min_height)

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example test cases
print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(max_area([1,1]))                # Output: 1


'''
Explanation of the Approach
Two-pointer technique: Start with one pointer at the beginning (left = 0) and the other at the end (right = len(height) - 1).
Compute the area formed by the two lines and update max_water if the new area is larger.
Move the pointer with the smaller height, since the water storage capacity depends on the smaller height. Moving the taller one won't increase the area.
Continue until the two pointers meet.
This approach ensures we check all potential areas without needing a brute-force O(n²) solution.
                                                                                   
Time Complexity Analysis
The algorithm iterates through the list once using the two-pointer approach, moving either the left or right pointer at each step.
Each element is processed at most once, making it an O(n) solution.
🔹 Time Complexity: O(n)
Since we traverse the array only once, this is the most efficient approach.

Space Complexity Analysis
The algorithm only uses constant extra space (left, right, and max_water variables).
No additional data structures are used.
🔹 Space Complexity: O(1)
The space required does not grow with input size.
'''

