""""Given list of integers, return array of one more than that.

Task: Given a non-empty array of decimal digits representing a non-negative
integer, increment one to the integer. The digits are stored such that the most
significant digit is at the head of the list, and each element in the array
contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.
"""


class Solution:
    """Adding 1 to array of integers."""

    def plusone(self, digits):
        """Adding 1 to array of integers."""
        # iterate from the right and add 1 if int != 9
        # add condition to account for digit[i] = 9
        carry_over = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9 and carry_over == 0:
                digits[i] += 1
                return digits
            elif digits[i] != 9 and carry_over == 1:
                digits[i] += carry_over
                return digits
            else:
                digits[i] = 0
                carry_over = 1
        # in case carry over is left over, add [1] to digits
        return [1] + digits
