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
        # print("must match value: ", val)
        # print("------------------------")
        while head:
            # print("res before: ", res)
            # print("current head is: ", head.val)
            # print("curr pointer is: ", curr.val)
            if head.val == val:
                if head.next is None:
                    # print("At the end of the road...")
                    curr.next = None
                    curr = curr.next
                else:
                    # print("match found, so continue")
                    pass
            else:
                # print("match not found, will update curr pointer")
                curr.next = head
                # print("curr will now point to ", head.val)
                curr = curr.next
            head = head.next
            # print("res after: ", res)
            # print()
        return res.next