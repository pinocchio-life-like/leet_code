
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while head and head.next:
        first = head
        second = head.next
        
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
        head = first.next
    
    return dummy.next
