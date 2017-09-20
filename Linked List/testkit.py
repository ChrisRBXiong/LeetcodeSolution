# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        string = ""
        p = self
        while p is not None:
            string += str(p.val) + " "
            p = p.next
        return string


def create_list(l):
    if len(l) == 0 or l is None:
        return None
    dummy_head = ListNode(0)
    p = dummy_head
    for e in l:
        p.next = ListNode(e)
        p = p.next
    return dummy_head.next

