"""Implement next permutation given array.

Rearrange numbers into the lexicographically next greater permutation of
numbers.
"""


class Solution:
    """Find next permuation without creating new array."""

    def nextpermutation(self, nums):
        """Do not return anything, modify nums in-place instead."""
        # Create swap and reverse functions to replace numbers
        # and only use extra memory

        def swap(arr, a):
            """Function swap positions of element with num just larger it."""
            # iterate through right of the arr to find num closest to a
            n = len(arr)
            mini = 10000000
            for i in range(a + 1, n):
                if arr[i] > arr[a]:
                    mini = min(mini, arr[i])
            # swap a with mini value
            for i in range(a + 1, n):
                # in case of multiple mini values take the far right one
                if (arr[i] == mini and i == n - 1) or \
                   (arr[i] == mini and arr[i + 1] != mini):
                    arr[i], arr[a] = arr[a], arr[i]
                    break

        def reverse(arr, k):
            """Function reverse given array with starting k position."""
            n = len(arr)
            j = n - 1
            while k < j:
                arr[k], arr[j] = arr[j], arr[k]
                k += 1
                j -= 1

        # Start from right end and make needed swap and reverse rest of array
        # From right numbers should acsend. If not, swap that i position
        # and reverse of array to the right
        n = len(nums)
        p = 0  # test if arrangement is possible
        # move j left to find descending adjacent numbers
        for j in range(n - 2, -1, -1):
            if nums[j] < nums[j + 1]:
                swap(nums, j)
                reverse(nums, j + 1)
                p += 1
                break
        # check if not possible
        if p == 0:
            reverse(nums, 0)
