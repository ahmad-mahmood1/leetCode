# ListNode is LeetCode's implementation of a Linked List
def hasCycle(head) -> bool:
    # edge case: head is empty - no cycle
    if not head:
        return False
        
    # Define slow and fast pointers
    slow, fast = head, head.next
        
    # As long as both pointers don't meet...
    while slow != fast:
        # If fast pointer has reached the end of the list, no cycle
        if not fast or not fast.next:
            return False
                
        slow = slow.next # slow pointer moves forward 1 step
        fast = fast.next.next # fast pointer moves forward 2 steps
        
    # Didn't reach end of list, there was a cycle
    return True