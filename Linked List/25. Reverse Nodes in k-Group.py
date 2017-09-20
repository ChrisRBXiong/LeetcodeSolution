'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

from testkit import *

'''Solution 1'''
class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        new_head = self.sub_reverse_iteration(head,k)
        last_tail, sub_head = head, head.next
        while sub_head is not None:
            new_sub_head = self.sub_reverse_iteration(sub_head,k)
            last_tail.next = new_sub_head
            last_tail, sub_head = sub_head, sub_head.next
        return new_head


    def sub_reverse_iteration(self,head,k):
        """
        reverse given linked-list 'head' top-k elements, and return the new head node.
        iterative version
        """
        ## Calculate the length of given list.
        length = 0
        p = head
        while p is not None:
            p = p.next
            length += 1
        if length < k or length == 1:       # less than k or equal one, just return
            return head
        
        first, middle, last = head, head.next, head.next.next   # last may be None
        
        while middle is not None and k > 1:   #start reverse, After that, middle is the new head and head is the new tail
            middle.next = first
            first = middle
            middle = last
            last = last.next if last else None
            k -= 1
        
        head.next = middle      # for next function. just a temp pointer
            
        return first

'''Solution 2'''
class Solution2(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k < 2:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head

        head, tail, temp = dummy_head, dummy_head, None
        count = 0
        while tail is not None:
            for count in range(k):
                tail = tail.next
                if tail is None:
                    break
            else:
                original_head = head.next
                for count in range(k-1):
                    temp = head.next
                    head.next = temp.next
                    temp.next = tail.next
                    tail.next = temp
                
                tail = original_head
                head = original_head

        return dummy_head.next
            

                    
                    
        


        