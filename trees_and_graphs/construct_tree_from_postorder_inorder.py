"""Construct Binary Tree from Inorder and Postorder Traversal.

Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the same
tree, construct and return the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """Use postorder & inorder to build tree."""
        # Use postorder to find root
        if not inorder or not postorder:
            return None
        elif len(inorder) == 1 or len(postorder) == 1:
            # Move onto next root
            postorder.pop()
            return TreeNode(inorder[0])
        else:
            # The head will be last int in postorder
            head = postorder[-1]
            root = TreeNode(head)

            # split inorder list into two trees
            leftSide = inorder[:inorder.index(head)]
            rightSide = inorder[inorder.index(head) + 1:]

            # Move onto next root from postorder
            postorder.pop()

            # Start from rightSide since postorder will always be there
            root.right = self.buildTree(rightSide, postorder)
            root.left = self.buildTree(leftSide, postorder)

            return root
