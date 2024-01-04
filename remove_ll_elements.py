from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        curr.next = head
        while head:
            print("-------------------------")
            print("head is: ", head)
            print("current is: ", curr)
            print("-------------------------")
            if head.next is not None:
                if head.next.val == val:
                    print("Match")
                    temp = head.next.next
                    head.next = temp
            else:
                if head.val == val:
                    break
            head = head.next
            print("new head is: ", head)
            curr = curr.next
            print("new current is: ", curr)
            print("Res: ", res)
        print("After while loop: ", curr)
        return res.next
        