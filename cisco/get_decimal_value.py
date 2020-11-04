"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""


def getDecimalValue( head: ListNode) -> int:
    n = 0
    decimal = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next

    while head:
        if head.val == 1:
            decimal += 2**(n-1)
        n -= 1
        head = head.next
    return decimal

