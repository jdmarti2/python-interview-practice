"""Given an integer array nums, return all the triplets equal to zero."""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            """Find all groups of 3ints in array that equal 0."""
        def twosum(arr, target):
            """Find two ints in array that sum = target."""
            d = {}
            # Create set of triplets to avoid duplicates
            triplets = set()
            for i, num in enumerate(arr):
                # search for goal = target - num
                goal = target - num
                if goal not in d:
                    d[num] = i
                else:
                    triplets.add((-target, num, goal))
            return triplets

        if len(nums) < 3:
            return []
        nums = sorted(nums)
        results = set()
        # Use logic from twosum
        # iterate through nums with -x target to find triplets/results
        for x in range(len(nums) - 2):
            pairs = twosum(nums[(x + 1):], -nums[x])
            results = set.union(results, pairs)

        return results
