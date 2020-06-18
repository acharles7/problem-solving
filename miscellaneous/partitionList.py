'''
Given a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

# Two pass
def partition(head: ListNode, x: int) -> ListNode:
    before, after = [], []
    while head: 
        if head.val < x:
            before.append(head.val)
        else:
            after.append(head.val)
        head = head.next

    sentinel = curr = ListNode(0)
    for num in before+after:
        curr.next = ListNode(num)
        curr = curr.next
    return sentinel.next

# One pass 
def partition(head: ListNode, x: int) -> ListNode:

    before = curr1 = ListNode(-1)
    after = curr2 = ListNode(-1)

    while head: 
        if head.val < x:
            curr1.next = ListNode(head.val)
            curr1 = curr1.next
        else:
            curr2.next = ListNode(head.val)
            curr2 = curr2.next
        head = head.next
    curr1.next = after.next
    return before.next
