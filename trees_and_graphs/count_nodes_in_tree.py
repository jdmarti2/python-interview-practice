"""Count Complete Tree Nodes in < O(n) time.

Task: Given the root of a complete binary tree, return the number of the nodes
in the tree. According to Wikipedia, every level, except possibly the last, is
completely filled in a complete binary tree, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at
the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        # iterate through last level in tree
        for _ in range(d):
            # make pivot the mid point (round down)
            pivot = left + (right - left) // 2
            # if idx is located on left side, make pivot new right/end
            if idx <= pivot:
                # must be in left subtree
                node = node.left
                right = pivot
            # if idc is located on right side, make left right of pivot
            else:
                # must be in right subtree
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        print(d)
        print((2**d - 1))
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left
