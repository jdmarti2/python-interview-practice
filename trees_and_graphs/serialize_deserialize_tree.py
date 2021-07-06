"""Serialize and Deserialize Binary Tree.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root, traversal):
            """Use preorder traversal to code tree to str."""
            if not root:
                traversal += str(None) + ','
            else:
                traversal += str(root.val) + ','
                traversal = preorder(root.left, traversal)
                traversal = preorder(root.right, traversal)
            return traversal
        return preorder(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(data_lis):
            """Take list of coded str and convert back to Tree."""
            if data_lis[0] == 'None':
                data_lis.pop(0)
            else:
                root = TreeNode(int(data_lis[0]))
                # Remove element from list
                data_lis.pop(0)
                # Recursively fill in the branches
                root.left = helper(data_lis)
                root.right = helper(data_lis)
                return root

        # prep data to list format
        data_lis = [i for i in data.split(',')]
        # Remove last comma from data_lis
        data_lis.pop()

        return helper(data_lis)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
