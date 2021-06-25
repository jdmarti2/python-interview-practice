"""Return product of two strings integers as a string.

Task: Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to
integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Use old school long multiplication."""
        # convert str to int thru iterating through string
        first_num = 0
        second_num = 0
        for i in range(len(num1)):
            first_num += (int(num1[i]) * (10**(len(num1)-(i+1))))
        for j in range(len(num2)):
            second_num += (int(num2[j]) * (10**(len(num2)-(j+1))))
        return(str(first_num*second_num))
