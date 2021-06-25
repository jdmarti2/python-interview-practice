"""Construct a deep copy of the list.

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Task: Construct a deep copy of the list. Deep copy should consist of exactly
n brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.
"""


class Node:
    """Definition for a Node."""

    def __init__(self, x, next=None, random=None):
        """Definition for a Node."""
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """Construct deep copy of linked list."""

    def __init__(self):
        """Dict which holds old nodes as keys and new nodes as its values."""
        self.visitedHash = {}

    def copyrandomlist(self, head):
        """Copy random Linked list."""
        # If list is empty return empty list
        if not head:
            return head

        # If we already processed the current node, return the cloned version
        if head in self.visitedHash:
            return self.visitedHash[head]

        # If node not already processed create a new one with same value as old
        node = Node(head.val)

        # Save value in hash map
        self.visitedHash[head] = node

        # Copy recursively the remaining linked list starting once from the
        # next pointer and then from the random pointer
        # Two independent recursive calls
        # Update the next and random pointers for the new node created
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
