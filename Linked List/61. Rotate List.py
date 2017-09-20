'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        original_last, new_last = head, head
        length = 1
        while original_last.next is not None:
            length += 1
            original_last = original_last.next
        for i in range(length - (k % length) - 1):
            new_last = new_last.next
        
        original_last.next = head
        new_head = new_last.next if new_last.next else head
        new_last.next = None
        return new_head
        
            
            
            
        
        



        
        
