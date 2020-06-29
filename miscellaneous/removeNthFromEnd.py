'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    psuedo = ListNode(-1)
    psuedo.next = head
    slow, fast = psuedo, psuedo

    for i in range(n):
        fast = fast.next   

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return psuedo.next
