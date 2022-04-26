# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        first_value, extra = self.sumValues(l1.val, l2.val)        
        l3 = ListNode(first_value)
        temp_l3 = l3
        
        next_l1 = l1
        next_l2 = l2
        
        while True:
            
            next_l1 = self.getNextNode(next_l1)
            next_l2 = self.getNextNode(next_l2)

            if next_l1 is None and next_l2 is None:
                
                if extra > 0:
                    temp_l3.next = ListNode(extra)
                    
                break

            val_1 = self.getNextValue(next_l1)
            val_2 = self.getNextValue(next_l2)
            
            val_3, extra = self.sumValues(val_1, val_2, extra)
            
            temp_l3.next = ListNode(val_3)
            temp_l3 = temp_l3.next
                
        return l3
        
    def sumValues(self, l1_val, l2_val, extra=0):
        total = l1_val + l2_val + extra
        value = total % 10
        extraDigit = 0
        
        if(total >= 10) :
            extraDigit = 1
        
        return value, extraDigit
    
    def getNextNode(self, next_ln):
        node = None
        
        if next_ln is not None:
            node = next_ln.next
        
        return node
    
    def getNextValue(self, next_ln):
        value = 0
        
        if next_ln is not None:
            value = next_ln.val
        
        return value
    
        