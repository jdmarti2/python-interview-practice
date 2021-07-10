"""Maximize Distance to Closest Person.

You are given an array representing a row of seats where seats[i] = 1
represents a person sitting in the ith seat, and seats[i] = 0 represents that
the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the
closest person to him is maximized. 

Return that maximum distance to the closest person.
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        d = {}
        # hash all taken seats
        for i, v in enumerate(seats):
            if v == 1:
                d[i] = v
        # make list of d keys
        keys = []
        for a, b in d.items():
            keys.append(a)
        # if only 1 seat taken, one of the ends must be the farthest open seat
        if len(keys) == 1:
            return max(abs(keys[0] - len(seats) + 1), keys[0])
        # if more than 1 seat taken, find the biggest gap
        # Initialize max difference to furthest point from endpoint
        max_diff = max(keys[0], (len(seats) - 1) - keys[-1])
        # use 2 pointers to iterate through keys to find max difference
        left, right = 0, 1
        while right < len(keys):
            max_diff = max(max_diff, (keys[right] - keys[left]) // 2)
            right += 1
            left += 1
        return max_diff
