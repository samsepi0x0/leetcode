# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def list2num(self, list):
        sum = ""
        while list is not None:
            sum += str(list.val)
            list = list.next
        return int(sum[::-1])
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        sum = str(num1+num2)[::-1]
        
        first = None
        previous = None
        for i in sum:
            current = ListNode(i)
            if first is None:
                first = current
            if previous is not None:
                previous.next = current
            previous = current
        return first
        
