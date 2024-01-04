class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # Find the lengths of both linked lists
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        
        # Reset the pointers to the heads of the linked lists
        currA, currB = headA, headB
        
        # Move the pointers to align the starting positions
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
        
        # Move both pointers simultaneously until they meet at the intersection point
        while currA != currB:
            currA = currA.next
            currB = currB.next
        
        return currA
