'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''

def isPalindrome(head):
    # STEP 1: Find middle using fast & slow pointers
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # STEP 2: Reverse the second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    # STEP 3: Compare first half with reversed second half
    left = head
    right = prev  # prev is the head of reversed second half
    
    while right:  # Check right because second half might be shorter
        if left.val != right.val:  # Values don't match!
            return False
        left = left.next
        right = right.next
    
    return True  # All values matched!