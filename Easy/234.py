


class ListNode:     
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    l1 = []
    while node is not None:
        l1.append(node.val)
        node = head.next

    result = False
    
    if l1 == l1[::-1]:  
        result = True

    return result

