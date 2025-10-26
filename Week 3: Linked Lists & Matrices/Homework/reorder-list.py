'Given a linked list, rearrange it so you alternate between taking from the start and the end.'

def reorderList(head):
    if not head or not head.next:
        return
    
    # Step 1: Find middle
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    prev = None
    current = slow
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Step 3: Merge two halves
    first = head
    second = prev
    
    while second.next:
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2