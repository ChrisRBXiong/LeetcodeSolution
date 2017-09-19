# Definition for singly-linked list.
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
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
        dummy_head = ListNode(0)                        #哑的头结点
        cur_l1, cur_l2, cur_res = l1, l2, dummy_head
        carry = 0                                       #进位

        while cur_l1 is not None or cur_l2 is not None or carry != 0:
            x = cur_l1.val if cur_l1 else 0
            y = cur_l2.val if cur_l2 else 0
            sum_val = x + y + carry
            carry = sum_val / 10
            cur_res.next = ListNode(sum_val % 10)
            cur_res = cur_res.next
            if cur_l1 is not None:  cur_l1 = cur_l1.next
            if cur_l2 is not None:  cur_l2 = cur_l2.next
        
        return dummy_head.next



    
        
        

