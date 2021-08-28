"""Linked List Cycle.

Task: Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findIntersect(self, head):
        """Use Two pointers to find if cycle exists."""
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return slow
        return None
    
    
    def detectCycle(self, head: ListNode) -> ListNode:
        """Use Two pointers to find if cycle exists."""
        if head is None:
            return None
        
        curr = head
        intersect = self.findIntersect(head)
        
        if intersect is None:
            return
        
        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        while curr != intersect:
            curr = curr.next
            intersect = intersect.next
        return curr
