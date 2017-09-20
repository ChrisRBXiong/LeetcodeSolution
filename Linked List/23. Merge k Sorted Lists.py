"""
Merge k sorted linked lists and return it as one sorted list.
"""
from testkit import *
from queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        cur_head = dummy_head
        nodes_pq = PriorityQueue()
        for head in lists:
            if head: 
                nodes_pq.put_nowait((head.val, head))
        while nodes_pq.qsize() > 0:
            node = nodes_pq.get_nowait()
            cur_head.next = node
            node = node.next
            if node: nodes_pq.put_nowait((node.val,node))
        return dummy_head.next
        
            