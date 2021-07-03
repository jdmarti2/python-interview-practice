"""Diameter of Binary Tree.

Task: Given the root of a binary tree, return the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root. The
length of a path between two nodes is represented by the number of edges
between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        # Get max path from left and right sides from every node
        def maxPath(root):
            nonlocal diameter
            # if leaf return 0
            if not root:
                return 0
            leftpath = maxPath(root.left)
            rightpath = maxPath(root.right)
            diameter = max(diameter, leftpath + rightpath)
            return max(leftpath, rightpath) + 1

        diameter = 0
        maxPath(root)
        return diameter
