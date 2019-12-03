"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists_v1(self, l1, l2):
        head = ListNode(0)
        tail = head
        while l1 is not None and l2 is not None:
            left = l1.val < l2.val
            tail.next = l1 if left else l2
            tail = tail.next
            l1 = l1.next if left else l1
            l2 = l2 if left else l2.next
            tail.next = l2 if l1 is None else l1
        return head.next
    
    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev_head = ListNode(0)
        curr = prev_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        ## l1 or l2 is None.
        while l1:
            curr.next = ListNode(l1.val)
            l1 = l1.next
            curr = curr.next
        while l2:
            curr.next = ListNode(l2.val)
            l2 = l2.next
            curr = curr.next
        return prev_head.next

    def mergeTwoLists_v3(self, l1: ListNode, l2: ListNode) -> ListNode:
        # establish the head as the lower value
        if not l1 or not l2: return l1 or l2
        n1, n2 = (l1,l2) if l1.val < l2.val else (l2,l1)
        head = n1
        prev, n1 = n1, n1.next
        while n1 and n2:
            if n1.val < n2.val:
                prev.next = n1
                n1 = n1.next
            else:
                prev.next = n2
                n2 = n2.next
            prev = prev.next
        prev.next = n1 or n2
        return head