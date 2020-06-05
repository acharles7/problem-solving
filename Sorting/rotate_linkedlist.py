# Given a linked list, rotate the list to the right by k places, where k is non-negative.

def rotateRight(head, k) -> ListNode:
    lst = []
    if not head: return None
    while head:
        lst.append(head.val)
        head= head.next

    n = k % len(lst) if k > len(lst) else k
    lst = lst[-n:] + lst[:-n]

    root = ListNode(-1)
    psuedo = root
    for node in lst:
        psuedo.next = ListNode(node)
        psuedo = psuedo.next
    return root.next
