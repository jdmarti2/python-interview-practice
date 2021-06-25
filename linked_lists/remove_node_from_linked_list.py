"""Remove the nth node from the end of a linked list.

Task: Given the head of a linked list, remove the nth node from the end of the
list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	"""Removing node from linked list."""

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Use two pass system to skip the ith node"""
        # Get length of head
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        # get target position from length and n
        target = length - n
        
        # Define i for index, previous and current nodes
        i = 0
        node = head
        dummy_head = tail = ListNode()
        
        # iterate through nodes until i = target
        while i < target:
            #print("i", i)
            #print("tail", tail)
            #print("node", node)
            #print("dummy_head", dummy_head)
            tail.next = ListNode(node.val)
            node = node.next
            tail = tail.next
            i += 1

        # Connect node.next (after target) and connect to tail
        tail.next = node.next
        
        return dummy_head.next           
        