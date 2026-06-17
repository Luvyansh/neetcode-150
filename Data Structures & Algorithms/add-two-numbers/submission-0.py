# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1 or l2:
            if l1:
                num1.append(l1.val)
                l1 = l1.next
            if l2:
                num2.append(l2.val)
                l2 = l2.next
        
        result = []
        carry = 0
        i, j = 0, 0
        
        while i < len(num1) or j < len(num2) or carry:
            digit1 = num1[i] if i < len(num1) else 0
            digit2 = num2[j] if j < len(num2) else 0
            
            total_sum = digit1 + digit2 + carry
            
            carry = total_sum // 10
            result.append(total_sum % 10)
            
            i += 1
            j += 1

        dum = ListNode()
        cur = dum
        for i in result:
            cur.next = ListNode(i)
            cur = cur.next
        return dum.next