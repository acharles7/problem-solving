'''
Given a singly linked list, determine if it is a palindrome.

Could you do it in O(n) time and O(1) space?
'''

# Time O(n), Space O(n)

def is_palindrome(head):
    s = []
    while head:
        s.append(head.val)
        head = head.next

    l, r = 0, len(s)-1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


# Time O(n), Space O(1)

def get_first_end(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    
def reverse(self, head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
                        
    
def isPalindrome(self, head: ListNode) -> bool:

    if not head: return True

    first_end = self.get_first_end(head)
    second_start = self.reverse(first_end.next)

    first = head
    second = second_start

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True

