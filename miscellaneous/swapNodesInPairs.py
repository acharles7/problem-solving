'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative
def swapPairs(head: ListNode) -> ListNode:
    temp = ListNode(-1)
    temp.next = head
    prev = temp

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next
    return temp.next

# Recursive 
def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    first = head
    second = head.next

    first.next = self.swapPairs(second.next)
    second.next = first
    return second
