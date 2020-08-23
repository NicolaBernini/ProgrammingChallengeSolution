# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sum_digits(self, l1, l2, c=0):
        temp = c 
        if l1 is not None: temp += l1.val
        if l2 is not None: temp += l2.val
        return ListNode(val=temp%10), temp//10
    
    def add_to_queue(self, head, node):
        if head is None: return node
        temp = head
        while temp.next is not None: temp = temp.next
        temp.next = node
        return head
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        c = 0
        while not (l1 is None and l2 is None):
            temp,c = self.sum_digits(l1=l1, l2=l2, c=c)
            res = self.add_to_queue(res, temp)
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        if c>0: res = self.add_to_queue(res, ListNode(val=c))
        return res 

