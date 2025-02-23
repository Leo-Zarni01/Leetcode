from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        ## create two pointers,
        current_node = head
        previous_node = None

        ## traverse
        while current_node.next is not None:
            ## keep track of next node 
            next_node = current_node.next
            
            ## here comes the tricky part, manipulating the pointers
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        head = previous_node
        return head
