# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    curr = ListNode(-1)
    res = curr

    while l1 and l2:
        if l1.val <= l2.val:
            res.next = l1
            l1 = l1.next
        else:
            res.next = l2
            l2 = l2.next
        res = res.next

    res.next = l2 if l1 is None else l1
    return curr.next
