"""Closest Binary Search tree Value.

Task: Given the root of a binary search tree and a target value, return the
value in the BST that is closest to the target.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Closest Binary Search Tree Value."""

    def closestValue(self, root, target):
        """Closest Binary Search tree Value."""
        def closestHelper(root, target):
            nonlocal mindic
            if not root:
                # if target not in root return the next best
                return min(mindic, key=mindic.get)
            if root.val == target:
                return target
            # if target is smaller than node go left
            if target < root.val:
                # hash the difference
                bestmin = root.val - target
                mindic[root.val] = bestmin
                return closestHelper(root.left, target)
            elif target > root.val:
                # hash the difference
                bestmin = target - root.val
                mindic[root.val] = bestmin
                return closestHelper(root.right, target)

        # Hash map the min val if target not in root
        mindic = {}
        return int(closestHelper(root, target))
