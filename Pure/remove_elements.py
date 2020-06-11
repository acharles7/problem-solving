"""
Remove all elements from a linked list of integers that have value val.
"""

def removeElements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head

    curr, prev = head, sentinel
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return sentinel.next
