"""Given the root of a binary tree, return the maximum path sum of any path.

TASK: A path in a binary tree is a sequence of nodes where each pair of
adjacent nodes in the sequence has an edge connecting them. A node can only
appear in the sequence at most once. Note that the path does not need to pass
through the root.

The path sum of a path is the sum of the node's values in the path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Findind the max path."""

    def maxPathSum(self, root):
        """Return path with max potential."""
        def maxPotential(node):
            """Return max potention from each node in tree."""
            nonlocal maxsum
            # Allocate null values to 0
            if not node:
                return 0

            # Get the max sum from the left and right subtrees
            # We only care about possible gains (no negative values)
            # Iterates all the way to the far left
            left_max = max(maxPotential(node.left), 0)
            print("left_max:", left_max)
            # Iterates down the recursive stack
            right_max = max(maxPotential(node.right), 0)
            print("right_max:", right_max)

            # Get sum of potential
            potential = node.val + left_max + right_max
            print("potential", potential)

            # Update new maxsum
            maxsum = max(maxsum, potential)

            # Recursively return the max potential if continue on same path
            return node.val + max(left_max, right_max)

        # Initialize maxsum to negative infinity
        maxsum = float('-inf')
        maxPotential(root)

        return maxsum
