"""Add the integers from two linked lists together.

Task: You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.
"""


class ListNode:
	"""Definition for singly-linked list."""_

    def __init__(self, val=0, next=None):
    	"""Definition for singly-linked list."""
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers from linked list"""
        # Create a placeholder for the result
        dummy_head = tail = ListNode()
        
        # Define carry_over in case of sum > 9
        carry_over = 0
        while l1 or l2:
            if not l2:
                summ = carry_over + l1.val
            elif not l1:
                summ = carry_over + l2.val
            else:
                summ = carry_over + l1.val + l2.val

            if summ > 9:
                tail.next = ListNode(summ % 10)
                carry_over = 1
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            else:
                tail.next = ListNode(summ % 10)
                carry_over = 0
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            # Set new tail and iterate again to find new tail.next
            tail = tail.next
        
        # Check if carry_over = 1 after loop
        if carry_over == 1:
            tail.next = ListNode(carry_over)

        return dummy_head.next
