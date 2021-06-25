"""Given array of jumps, see if you can make it to the end.

Task: Given an array of non-negative integers nums, you are initially
positioned at the first index of the array. Each element in the array represents
your maximum jump length at that position. Determine if you are able to reach
the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Use recursive approach and work backwards.
        # Find good last positions
        last_pos = len(nums) - 1
        # Start from second to last position and go left to find good positions
        for i in range((len(nums) - 2), -1, -1):
            # Check if current position can reach last position
            # if so, current position is new last position
            if i + nums[i] >= last_pos:
                last_pos = i
        # Check and see if first index could be last position
        if last_pos == 0:
            return True
        else:
            return False
