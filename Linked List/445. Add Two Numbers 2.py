'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)                            #哑的头结点
        p_stack, q_stack = [], []
        while l1 is not None:
            p_stack.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            q_stack.append(l2.val)
            l2 = l2.next
        carry = 0

        while len(p_stack) or len(q_stack) or carry:
            x = p_stack[-1] if len(p_stack) else 0
            y = q_stack[-1] if len(q_stack) else 0
            sum_val = x + y + carry
            carry = sum_val // 10
            
            cur_node = ListNode(sum_val % 10)
            cur_node.next = dummy_head.next
            dummy_head.next = cur_node

            if len(p_stack): p_stack.pop() 
            if len(q_stack): q_stack.pop()
        
        return dummy_head.next
        
            
            



        

