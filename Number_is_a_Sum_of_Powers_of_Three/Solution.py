'''
Approach:
A number can be represented as the sum of distinct powers of three if, when converted to base 3, it contains only 0s and 1s (i.e., no 2s).
We repeatedly divide n by 3, checking that the remainder is never 2.
'''

class PowerOfThreeChecker:
    def __init__(self, n: int):
        self.n = n

    def check_powers_of_three(self) -> bool:
        """Check if n can be represented as a sum of distinct powers of three."""
        n = self.n
        while n > 0:
            if n % 3 == 2:  # If remainder is 2, it's not possible
                return False
            n //= 3  # Move to the next power of three
        return True

# Example Usage
checker1 = PowerOfThreeChecker(12)
print(checker1.check_powers_of_three())  # Output: True

checker2 = PowerOfThreeChecker(91)
print(checker2.check_powers_of_three())  # Output: True

checker3 = PowerOfThreeChecker(21)
print(checker3.check_powers_of_three())  # Output: False

''' 
Time Complexity Analysis:
The number of iterations in the while loop is O(log₃(n)), since n is divided by 3 in each step.
Given n ≤ 10⁷, the worst case is around log₃(10⁷) ≈ 14 iterations, which is very efficient.
Overall complexity: O(log n) (base 3).
Space Complexity:
O(1), as we use only a few integer variables.
'''