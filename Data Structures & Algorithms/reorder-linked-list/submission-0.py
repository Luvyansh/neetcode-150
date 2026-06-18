# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Brute Force
        li = list()
        res = list()
        n = 0
        temp = head
        while temp:
            print(temp.val)
            li.append(temp.val)
            n += 1
            temp = temp.next
        i = 0
        while True:
            if i>=n/2:
                break
            res.append(li[i])
            res.append(li[n-1-i])
            i += 1
        print(n, " ; ", li, " ; ", res)
        for i in range(1, n):
            head.next = ListNode(res[i])
            head = head.next