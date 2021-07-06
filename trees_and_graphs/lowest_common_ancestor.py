"""Lowest Common Ancestor of a Binary Tree.

Task: Given a binary tree, find the lowest common ancestor (LCA) of two given
nodes in the tree.

According to the definition of LCA on Wikipedia: 'The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).'
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        # traversal to return root.val if = p or q 
        if root.val in (p.val, q.val):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # Ancestors inherit correct child nodes
        if left and right:
            return root
        elif left or right:
            return left or right
