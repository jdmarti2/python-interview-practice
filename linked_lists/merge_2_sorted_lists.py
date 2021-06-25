"""Merge two sorted linked lists and return it as a sorted list."""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        """Definition for singly-linked list."""
        self.val = val
        self.next = next


class Solution:
    """Splice together the nodes of the first two lists."""

    def mergetwolists(self, l1, l2):
        """Merge two sorted linked lists."""
        # Create a placeholder for the result
        dummy_head = tail = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        # Append the remaining nodes of l1 or l2
        tail.next = l1 or l2

        return dummy_head.next
