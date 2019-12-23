"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Linked list instance:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Int -> String -> Int Conversion method
class SolutionConversion:
    def to_rev_num(self, l: ListNode) -> int:
        num = ''
        while l:
            num += str(l.val)
            l = l.next
        return int(num[::-1])
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_int = SolutionConversion().to_rev_num(l1) + SolutionConversion().to_rev_num(l2)
        sum_s = str(sum_int)[::-1]
        # Constructing answer list
        head = prev = None
        for c in sum_s:
            node = ListNode(int(c))
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
        return head

# Math solution
"""
Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, 
which is the head of l1 and l2. Since each digit is in the range of 0…9, summing two digits may "overflow". 
For example 5+7=12. In this case, we set the current digit to 2 and bring over the carry=1 to the next iteration. 
Carry must be either 0 or 1 because the largest possible sum of two digits (including the carry) is 9+9+1=19.
"""
class SolutionMath:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Init dummy head for returning list
        dummy_head = ListNode(0)
        current = dummy_head
        # Assigning temp values of p and q to the heads of l1 and l2
        p, q = l1, l2
        # Init carry value to 0
        carry = 0
        # Traversing through the l1 and l2:
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0 
            sum_ = carry + x + y
            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy_head.next